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