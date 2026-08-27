from typing import List, Dict
from ddgs import DDGS

def execute_web_search(query: str, max_results: int = 3) -> List[Dict[str, str]]:
    """Executes live web search using DDGS."""
    try:
        results = []
        with DDGS() as ddgs:
            for r in ddgs.text(query, max_results=max_results):
                results.append({
                    "query": query,
                    "title": r.get("title", ""),
                    "url": r.get("href", ""),
                    "content": r.get("body", "")
                })
        return results if results else [{"query": query, "content": "No relevant search results found."}]
    except Exception as e:
        return [{"query": query, "content": f"Search execution fallback: {str(e)}"}]