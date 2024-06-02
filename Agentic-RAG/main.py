import os
import logging
from pprint import pprint
from os.path import join, dirname
from dotenv import load_dotenv
from typing_extensions import TypedDict
from typing import List
from langgraph.graph import END, StateGraph
from VectorDB import createVectorDB
from Grader import retrievalGrader, hallucinationGrader
from AnswerGen import generateResponse, decideToGenerate
from WebSearch import tavilyWebSearchTool

logger = logging.getLogger(__name__)
logging.basicConfig(filename='state.log', level=logging.INFO)    
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)
URLS = ["https://towardsdatascience.com/text-classification-sentiment-analysis-on-r-sgexams-4ea341134fba"]
FIRECRAWL_API_KEY = os.environ.get("FIRECRAWL_API_KEY")
TAVILLY_API_KEY = os.environ.get("TAVILY_API_KEY")

class LangGraphState(TypedDict):
    """
    Represents the state of RAG LLM model architecture

    Attributes:
        question => question input
        generation => response generated from LLM
        web_search => result from web search 
        documents: corpus of documents for embedding
    """
    question: str
    generation: str
    web_search: str
    documents: List[str]

def retrieve(state: dict):
    """
    This function retrieve documents from vectorstore

    Args:
        state: The current graph state
        retriever: retriever tool from vectorDB
        
    Returns:
        state: New key added to state, documents that contains retrieved documents
    """
    retriever = createVectorDB(URLS, 250, 0, FIRECRAWL_API_KEY)
    print("---RETRIEVE---")
    question = state["question"]
    documents = retriever.invoke(question)
    return {"documents": documents, "question": question}

def main():
    workflow = StateGraph(LangGraphState)

    # Define nodes
    workflow.add_node("websearch", tavilyWebSearchTool)
    workflow.add_node("retrieve", retrieve)  
    workflow.add_node("grade_documents", retrievalGrader)
    workflow.add_node("generate", generateResponse)

    # Build graph
    workflow.set_entry_point("retrieve")
    workflow.add_edge("retrieve", "grade_documents")
    workflow.add_conditional_edges(
        "grade_documents",
        decideToGenerate,
        {
            "websearch": "websearch",
            "generate": "generate"
        },
    )
    workflow.add_edge("websearch", "generate")
    workflow.add_conditional_edges(
        "generate",
        hallucinationGrader,
        {
            "not_supported": "generate",
            "useful": END,
            "not useful": "websearch",
        }
    )

    # COMPILE
    app = workflow.compile()

    # TESTING RAG
    inputs = {"question": "How to save LLM cost"}
    for output in app.stream(inputs):
        for key, value in output.items():
            pprint(f"Finished running: {key}")
    pprint(value["generation"])

if __name__ == "__main__":
    main()