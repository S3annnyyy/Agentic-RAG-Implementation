import os
import logging
from os.path import join, dirname
from dotenv import load_dotenv
from typing_extensions import TypedDict
from typing import List
from langchain.schema import Document
from langgraph.graph import END, StateGraph
from langchain_community.vectorstores.utils import filter_complex_metadata
from langchain_community.chat_models import ChatOllama
from VectorDB import createVectorDB
from Grader import retrievalGrader, hallucinationGrader, answerGrader
from AnswerGen import generateResponse
from WebSearch import tavilySearchTool

logger = logging.getLogger(__name__)
logging.basicConfig(filename='state.log', level=logging.INFO)    
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)
URLS = ["https://towardsdatascience.com/text-classification-sentiment-analysis-on-r-sgexams-4ea341134fba"]
FIRECRAWL_API_KEY = os.environ.get("FIRECRAWL_API_KEY")
TAVILLY_API_KEY = os.environ.get("TAVILY_API_KEY")
GEN_LLM = ChatOllama(model="llama3", temperature=0)

# def main():
#     retriever = createVectorDB(URLS, 250, 0, FIRECRAWL_API_KEY)  
#     output = retrievalGrader(retriever=retriever, question="What is sentiment analysis of Secondary school?")
#     print(output)

#     output, docs = generateResponse(retriever=retriever, llm=GEN_LLM, question="How to buy iphone 5")
#     print(output)

#     output2 = hallucinationGrader(output, docs)
#     print(output2)

#     output3 = answerGrader(output, docs)
#     print(output3)

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

def main():
    raise NotImplementedError

if __name__ == "__main__":
    main()