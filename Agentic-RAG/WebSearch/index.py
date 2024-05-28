from langchain_community.tools.tavily_search import TavilySearchResults

def tavilySearchTool(apiKey: str, topN: int):
    return TavilySearchResults(k=topN)