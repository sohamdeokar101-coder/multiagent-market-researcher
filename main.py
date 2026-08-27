import os
import logging
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.markdown import Markdown
from rich.prompt import Prompt
from src.graph import build_market_research_graph, save_report_to_disk

logging.basicConfig(level=logging.WARNING)
console = Console()

def render_step_history_table(history):
    """Renders a clean table showing agent workflow execution steps."""
    table = Table(title="🤖 AGENT WORKFLOW EXECUTION HISTORY", show_header=True, header_style="bold magenta")
    table.add_column("Step", justify="center", style="cyan", width=8)
    table.add_column("Agent & Action Completed", style="bold green")

    for idx, step in enumerate(history, 1):
        table.add_row(f"Step {idx}", step)

    console.print(table)

def main():
    console.clear()
    console.print(Panel.fit(
        "[bold cyan]🤖 Multi-Agent Market Research Assistant[/bold cyan]\n"
        "[dim]Powered by LangGraph + Local Ollama + DuckDuckGo Web Search[/dim]",
        border_style="bright_blue"
    ))
    
    # 1. Interactive User Input
    user_topic = Prompt.ask(
        "\n[bold yellow]Enter the business topic you want to research[/bold yellow]",
        default="Autonomous Electric Vehicles Market in Europe 2026"
    )
    
    console.print(f"\n🚀 Initiating research workflow for: [bold green]'{user_topic}'[/bold green]\n")
    
    initial_state = {
        "topic": user_topic,
        "search_queries": [],
        "raw_search_results": [],
        "analytical_insights": "",
        "final_markdown_report": "",
        "step_history": []
    }
    
    # 2. Build and Execute State Graph with Rich Progress Spinner
    graph = build_market_research_graph()
    
    with console.status("[bold yellow]Agents collaborating... (Researcher ➔ Analyst ➔ Writer)[/bold yellow]", spinner="dots"):
        final_state = graph.invoke(initial_state)
        
    print()
    # 3. Print Clean Workflow Summary Table
    render_step_history_table(final_state["step_history"])
    print()

    # 4. Save Report to Disk
    clean_filename = f"reports/{user_topic.lower().replace(' ', '_')[:30]}_report.md"
    report_path = save_report_to_disk(final_state["final_markdown_report"], filename=clean_filename)
    
    # 5. Display Formatted Markdown Report in Terminal
    console.print(Panel(
        Markdown(final_state["final_markdown_report"]),
        title="📄 EXECUTIVE MARKET RESEARCH REPORT",
        border_style="cyan",
        expand=True
    ))
    
    console.print(f"\n✅ [bold green]Report successfully generated and saved to:[/bold green] [underline]{report_path}[/underline]\n")

if __name__ == "__main__":
    main()