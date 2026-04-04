from tavily import TavilyClient
import os

tavily = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))


def tavily_search(query: str, max_results: int = 5):
    response = tavily.search(
        query=query,
        search_depth="advanced",
        max_results=max_results
    )

    raw_results = response.get("results", [])
    results = []

    for item in raw_results:
        title = item.get("title", "")
        url = item.get("url", "")
        content = item.get("content", "")

        results.append({
            "title": title,
            "url": url,
            "content": content
        })
    return results
