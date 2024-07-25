import langchain_community.chat_models.ollama as llmType
import langchain_core.vectorstores as rtrType 
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.chat_models import ChatOllama

LLM = ChatOllama(model="llama3", temperature=0)

ANSGEN_PROMPT = PromptTemplate(
    template="""<|begin_of_text|><|start_header_id|>system<|end_header_id|> You are an assistant for question-answering tasks.
    Use the following pieces of retrieved context to answer the question. If you don't know the answer, just say that you don't know.
    Use three sentences maximum and keep the answer concise <|eot_id|><|start_header_id|>user<|end_header_id|>
    Question: {question}
    Context: {context}
    Answer: <|eot_id|><|start_header_id|>assistant<|end_header_id|>""",
    input_variables=["question", "document"],
)

def generateResponse(state: dict):
    """
    This function generates an answer using RAG on retrieved documents 

    Args:
        state: Current state of graph

    Returns:
        state: New key added to state, generation that contains LLM response
    """
    print("---GENERATE RESPONSE---")
    question = state["question"]
    documents = state["documents"]

    rag_chain = ANSGEN_PROMPT | LLM | StrOutputParser()
    
    generation = rag_chain.invoke({"context": documents, "question": question})
    return {"documents": documents, "question": question, "generation": generation} 

# CONDITIONAL EDGE
def decideToGenerate(state: dict):
    """
    This function determines whether to generate an answer or add to web search

    Args:
        state: The current graph state

    Returns:
        str: Binary decision fo next node to call 
    """
    print("---ACCESS GRADED DOCUMENTS---")
    question = state["question"]
    filtered_documents = state["documents"]
    web_search = state["web_search"]
    
    if web_search == "Yes":
        print("---DECISION: ALL DOCUMENTS NOT RELEVANT TO QN, INCLUDE WEB SEARCH---")
        return "websearch"
    else:
        print("---DECISION: GENERATE ANSWER---")
        return "generate"