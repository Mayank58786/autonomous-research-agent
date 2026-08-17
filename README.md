# Autonomous Research Agent

An experimental agentic AI system that autonomously researches a given topic using planning, tool calling, multiple specialized agents, source evaluation, verification, and iterative reasoning.

## Project Status

🚧 V1 — Initial implementation

The project is being developed incrementally, with architectural and implementation decisions documented alongside the code.

## Goal

The goal is to build and understand an autonomous research system rather than a simple chatbot or single-purpose AI agent.

The system should eventually be able to:

- understand a research objective
- plan the research required
- select and use appropriate tools
- delegate research tasks
- gather and evaluate sources
- identify gaps and conflicting information
- verify important findings
- iterate when additional research is necessary
- synthesize the results into a structured report

## Documentation

- [Project Overview](docs/01-project-overview.md)
- [Architecture](docs/02-architecture.md)
- [Architecture & Technical Decisions](docs/03-decisions.md)

## Status

This repository is under active development.

## Development Setup

The project uses standard Python with a project-local virtual environment.

### Requirements

- Python 3.13
- Git
- GitHub

### Windows Setup

Create the virtual environment:

```py -3.13 -m venv .venv```


Activate it:

```.venv\Scripts\Activate.ps1```

Verify:

```python --version```

```python -m pip --version```

The virtual environment should be active while developing the project.

## Current Implementation

### V1 — Agent Baseline

The first implementation establishes a minimal AI agent using the OpenAI Agents SDK.

The current application:

- creates an `Agent`
- defines its instructions
- executes the agent using `Runner`
- accepts a fixed test question
- returns the model's response

The agent does not yet have external tools or autonomous research capabilities. These will be introduced incrementally in subsequent implementation steps.

## V1 — Tool Calling

The agent can now use a Python function as an external tool.

The tool is exposed to the agent through the OpenAI Agents SDK. The agent receives the available tool description and can decide whether to call it based on the user's request.

The current implementation demonstrates the basic agentic loop:

1. Receive a request.
2. Determine whether a tool is useful.
3. Call the tool when appropriate.
4. Receive the tool result.
5. Produce a final response.

The current tool is intentionally simple and local. It is used to validate the tool-calling mechanism before introducing external research tools such as web search.

## V1 — Web Research

The agent can now use web search as an external tool.

When a question requires current or external information, the agent can invoke the web search tool, receive search results, and use those results to construct its response.

The current implementation demonstrates:

1. User provides a research question.
2. Agent determines that external information is required.
3. Agent invokes web search.
4. Search results are returned to the agent.
5. Agent synthesizes the information into a response.

This is the first external tool in the system and establishes the foundation for autonomous research.