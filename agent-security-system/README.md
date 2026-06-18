# Agent Security Target System

This is the initial LangGraph target system for the AI agent security testing project.

Ollama is not integrated yet. The current version uses deterministic placeholder node logic so the graph structure, routing, state, tools, and logs can be tested first.

## Setup

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

## Run

```bash
python -m app.main "What is the company leave policy?"
python -m app.main "Send a mock email to HR about internship certificate"
python -m app.main "Check employee 102"
```

## Current Graph

```text
User Input
  -> Orchestrator Node
  -> Research Node / Action Node / Final Node
  -> Final Response
```

## Next Step

Replace the placeholder logic inside the nodes with Ollama-backed LLM calls.
