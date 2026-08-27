import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from src.state import ResearchState
from src.tools import execute_web_search

load_dotenv()

def get_llm():
    """Returns local Ollama LLM client via OpenAI-compatible endpoint."""
    base_url = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434/v1")
    model_name = os.getenv("OLLAMA_MODEL", "qwen3-vl:4b")
    return ChatOpenAI(
        base_url=base_url,
        api_key="ollama",
        model=model_name,
        temperature=0.1
    )

def researcher_agent(state: ResearchState) -> ResearchState:
    """Agent 1: Formulates search queries and gathers web data."""
    llm = get_llm()
    topic = state["topic"]
    
    prompt = f"Generate 2 concise web search queries to find market size, key drivers, and competitors for: '{topic}'. Separate queries with newlines."
    response = llm.invoke(prompt)
    
    raw_queries = response.content.strip().split("\n")
    queries = [q.strip("- ").strip() for q in raw_queries if q.strip()][:2]
    if not queries:
        queries = [f"{topic} market size growth forecast", f"{topic} key players competitors analysis"]
        
    results = []
    for q in queries:
        results.extend(execute_web_search(q))
        
    state["search_queries"] = queries
    state["raw_search_results"] = results
    state["step_history"].append(f"Researcher: Gathered web data for queries: {queries}")
    return state

def analyst_agent(state: ResearchState) -> ResearchState:
    """Agent 2: Synthesizes search results into structured analytical metrics."""
    llm = get_llm()
    topic = state["topic"]
    raw_data = state["raw_search_results"]
    
    prompt = f"""
    You are a Senior Market Analyst. Analyze the following web search data for '{topic}':
    {raw_data}
    
    Synthesize the information into clean, clear bullet points covering:
    1. Executive Summary & Market Valuation / Growth Rates
    2. Primary Market Drivers & Technological Trends
    3. Competitive Landscape (Top OEMs, Tech Firms, Regional Leaders)
    """
    response = llm.invoke(prompt)
    state["analytical_insights"] = response.content
    state["step_history"].append("Analyst: Synthesized web data into core market metrics.")
    return state

def writer_agent(state: ResearchState) -> ResearchState:
    """Agent 3: Compiles insights into a clean, executive Markdown report."""
    llm = get_llm()
    topic = state["topic"]
    insights = state["analytical_insights"]
    
    prompt = f"""
    You are an Executive Business Writer. Transform these market insights into a clean, professional Markdown report for topic: '{topic}'.
    
    Insights:
    {insights}
    
    Formatting Requirements:
    - Title: # 📊 Executive Market Analysis: {topic}
    - Section Headings: ## Executive Summary, ## Key Market Drivers, ## Competitive Landscape, ## Strategic Recommendations
    - Include a Markdown Table for Competitive Landscape
    - Use **bold text** for metrics, market values, and percentages
    - Add a final blockquote (>) summarizing the core strategic takeaway
    """
    response = llm.invoke(prompt)
    state["final_markdown_report"] = response.content
    state["step_history"].append("Writer: Formatted final executive Markdown report.")
    return state