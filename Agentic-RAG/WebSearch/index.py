from langchain_community.tools.tavily_search import TavilySearchResults
from langchain.schema import Document

def tavilyWebSearchTool(state: dict):
    """
    This function conducts web search based on question and change in state

    Args:
        state: Current graph state

    Returns:
        state: Appended web results to documents
    """
    print("---WEB SEARCH---")
    question = state["question"]
    documents = state["documents"]
    web_search_tool = TavilySearchResults(k=3) 

    documents_searched = web_search_tool.invoke({"query": question})
    web_results = "\n".join([document["content"] for document in documents_searched])
    web_results = Document(page_content=web_results)

    if documents is not None:
        documents.append(web_results)
    else:
        documents = [web_results]
    
    return {"documents": documents, "question": question}