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
    raise NotImplementedError