from typing import List, Dict, Any, TypedDict

class ResearchState(TypedDict):
    topic: str
    search_queries: List[str]
    raw_search_results: List[Dict[str, str]]
    analytical_insights: str
    final_markdown_report: str
    step_history: List[str]