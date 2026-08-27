from src.state import ResearchState
from src.graph import build_market_research_graph

def test_graph_compilation():
    graph = build_market_research_graph()
    assert graph is not None

def test_state_schema():
    state = ResearchState(
        topic="AI Chips",
        search_queries=[],
        raw_search_results=[],
        analytical_insights="",
        final_markdown_report="",
        step_history=[]
    )
    assert state["topic"] == "AI Chips"
    assert isinstance(state["step_history"], list)