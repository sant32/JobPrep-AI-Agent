from tavily import TavilyClient
import os

tavily = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))


def tavily_search(query: str, max_results: int = 5):
    response = tavily.search(
        query=query,
        search_depth="advanced",
        max_results=max_results
    )

    return response.get("results", [])