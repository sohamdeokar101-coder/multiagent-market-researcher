import os
from langgraph.graph import StateGraph, END
from src.state import ResearchState
from src.agents import researcher_agent, analyst_agent, writer_agent

def build_market_research_graph():
    """Builds and compiles the sequential LangGraph workflow."""
    workflow = StateGraph(ResearchState)
    
    # 1. Add Agent Nodes
    workflow.add_node("Researcher", researcher_agent)
    workflow.add_node("Analyst", analyst_agent)
    workflow.add_node("Writer", writer_agent)
    
    # 2. Define Control Flow Edges
    workflow.set_entry_point("Researcher")
    workflow.add_edge("Researcher", "Analyst")
    workflow.add_edge("Analyst", "Writer")
    workflow.add_edge("Writer", END)
    
    return workflow.compile()

def save_report_to_disk(report_md: str, filename: str = "reports/market_analysis_report.md") -> str:
    """Saves the generated markdown report to file."""
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, "w", encoding="utf-8") as f:
        f.write(report_md)
    return filename