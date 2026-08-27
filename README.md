# 🤖 Multi-Agent Market Research Assistant

[![Standard Readme Compliant](https://img.shields.io/badge/readme%20style-standard-brightgreen.svg?style=flat-square)](https://github.com/RichardLitt/standard-readme)
[![Python 3.11+](https://img.shields.io/badge/Python-3.11+-blue.svg?style=flat-square)](https://www.python.org/downloads/)
[![LangGraph](https://img.shields.io/badge/LangGraph-0.1+-orange.svg?style=flat-square)](https://github.com/langchain-ai/langgraph)
[![Ollama](https://img.shields.io/badge/Ollama-qwen3--vl:4b-black.svg?style=flat-square)](https://ollama.ai/)
[![PyTest](https://img.shields.io/badge/PyTest-Passed-brightgreen.svg?style=flat-square)](https://docs.pytest.org/)

An interactive multi-agent market research assistant built using **LangGraph**, **LangChain**, and local **Ollama** LLMs. The application prompts users for custom research topics, delegates tasks across three specialized AI agents (**Researcher**, **Analyst**, and **Writer**), executes live web queries via DuckDuckGo, and renders executive-ready Markdown reports in the console while saving them to disk.

## Table of Contents

- [Background](#background)
- [Architecture](#architecture)
- [Install](#install)
- [Usage](#usage)
- [Generator](#generator)
- [Badge](#badge)
- [Example READMEs](#example-readmes)
- [Related Efforts](#related-efforts)
- [Maintainers](#maintainers)
- [Contributing](#contributing)
- [Contributors](#contributors)
- [License](#license)

---

## Background

Conducting thorough market research requires multiple cognitive steps: formulating targeted search queries, sifting through raw web results to extract key figures, and structuring analytical findings into an executive report. 

This project implements a **Sequential Multi-Agent Graph Architecture** using **LangGraph**:
- **Agent 1 (Researcher):** Formulates targeted search queries and gathers live web data using DuckDuckGo Search API.
- **Agent 2 (Analyst):** Filters noise, extracts market size metrics, identifies competitive players, and compiles analytical drivers.
- **Agent 3 (Writer):** Formats synthesized insights into a Markdown report saved to disk (`reports/`).

---

## Architecture

```text
 ┌───────────────────────────────────────────────────────────────┐
 │               LangGraph Sequential State Graph                │
 │                                                               │
 │ ┌──────────────┐     State      ┌─────────────┐    State      │
 │ │  Researcher  │ ─────────────► │   Analyst   │ ───────────┐  │
 │ └──────┬───────┘                └─────────────┘            │  │
 └────────┼───────────────────────────────────────────────────┼──┘
          │                                                   ▼
          ▼                                           ┌──────────────┐
  [ DuckDuckGo Search ]                               │    Writer    │
                                                      └───────┬──────┘
                                                              │
                                                              ▼
                                                 [ Executive Report (.md) ]



Usage
1. Configure Environment (.env)
Ensure your local .env file points to your local Ollama endpoint:
OLLAMA_BASE_URL=http://localhost:11434/v1
OLLAMA_MODEL=qwen3-vl:4b

2. Run Master Orchestrator Pipeline
Launch the master script and type any business or market topic when prompted:
python main.py

3. Run Automated Unit Tests
Validate graph compilation and state schema functionality using PyTest:
python -m pytest


Generator
Executing python main.py triggers an interactive prompt, displays real-time agent step history, and generates a structured executive report:
1. Terminal Console & Step History Output
╭─────────────────────────────────────────────────────────────╮
│ 🤖 Multi-Agent Market Research Assistant                    │
│ Powered by LangGraph + Local Ollama + DuckDuckGo Web Search │
╰─────────────────────────────────────────────────────────────╯

Enter the business topic you want to research (Autonomous 
Electric Vehicles Market in Europe 2026): f1 event and champion        

🚀 Initiating research workflow for: 'f1 event and champion'

               🤖 AGENT WORKFLOW EXECUTION HISTORY               
┏━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃   Step   ┃ Agent & Action Completed                          ┃
┡━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│  Step 1  │ Researcher: Gathered web data for queries: ['f1   │
│          │ event and champion market size growth forecast',  │
│          │ 'f1 event and champion key players competitors    │
│          │ analysis']                                        │
│  Step 2  │ Analyst: Synthesized web data into core market    │
│          │ metrics.                                          │
│  Step 3  │ Writer: Formatted final executive Markdown        │
│          │ report.                                           │
└──────────┴───────────────────────────────────────────────────┘

2. Rendered Executive Report Output (reports/f1_event_and_champion_report.md)
╭──────────── 📄 EXECUTIVE MARKET RESEARCH REPORT ─────────────╮
│      📊 Executive Market Analysis: f1 event and champion     │
│                                                              │
│ Executive Summary                                            │
│ F1’s global market is experiencing robust expansion, with a  │
│ $3.6 Billion valuation in 2024 driven by sustained fan       │
│ engagement and commercialization. Projected growth indicates │
│ a CAGR of 7% (2024–2031), reaching $5.6 Billion by 2031.     │
│                                                              │
│ ------------------------------------------------------------ │
│                                                              │
│ Key Market Drivers                                           │
│  • Rising Global Audience Engagement: Unparalleled           │
│    viewership growth via streaming and telemetry dashboards. │
│  • Commercialization Expansion: Strategic partnerships with  │
│    automotive brands and multi-year sponsorships.            │
│                                                              │
│ Competitive Landscape                                        │
│  • Top Teams: Mercedes, Red Bull, McLaren, Ferrari           │
│  • Tech & Data Players: Real-time analytics platforms        │
│                                                              │
│ Strategic Recommendations                                    │
│  1. Accelerate Digital Monetization via AR/VR fan tools.     │
│  2. Expand Asian Markets to capture new demographics.        │
╰──────────────────────────────────────────────────────────────╯

✅ Report successfully generated and saved to: 
reports/f1_event_and_champion_report.md


