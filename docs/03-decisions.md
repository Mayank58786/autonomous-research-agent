# 3. Technical Decisions

## Decision 001 — Use Git from the Beginning

### Decision

The project will use Git and GitHub from the beginning of development.

### Reason

Version control allows the project to:

- preserve implementation history
- revert unsuccessful experiments
- compare architectural changes
- document development milestones
- provide a reproducible project history

### Status

Accepted

---

## Decision 002 — Build Incrementally

### Decision

The system will be implemented in small, independently testable stages.

### Reason

Agentic systems can become complex quickly.

Incremental implementation makes it possible to distinguish problems caused by:

- the model
- prompts
- tools
- orchestration
- application code
- architecture

### Status

Accepted

---

## Decision 003 — Local Development

### Decision

Development will initially take place locally using a Windows development environment and a local IDE.

### Reason

Local development provides direct control over:

- source code
- dependencies
- environment variables
- debugging
- testing
- Git
- future deployment

### Status

Accepted

---

## Decision 004 — Agentic System Rather Than Single Agent

### Decision

The project will be designed as an agentic system that may contain multiple specialized agents rather than treating a single model call as the complete application.

### Reason

The objective of the project is to explore autonomous planning, tool usage, delegation, evaluation, and iteration.

### Status

Accepted

## Decision 005 — Standard Python Virtual Environment

### Decision

Use standard Python 3.13 with a project-local virtual environment (`.venv`) instead of Conda.

### Reason

The project does not require Conda. A standard Python virtual environment provides isolated dependencies while keeping the development setup simple and close to typical Python development and deployment environments.

### Status

Accepted

---

## Decision 006 — Use the OpenAI Agents SDK

### Decision

Use the OpenAI Agents SDK as the initial framework for implementing the agentic system.

### Reason

The SDK provides core primitives required by the project, including agents, execution through a runner, tool integration, and support for multi-agent orchestration.

Using these primitives allows the project to focus on agentic system design rather than implementing the underlying agent execution loop from scratch.

The SDK will be evaluated continuously as the architecture develops. If it becomes a limitation, the decision can be revisited.

### Status

Accepted

---

## Decision 007 — Validate Tool Calling with a Local Tool

### Decision

Validate the agent tool-calling architecture using a deterministic local Python function before introducing external tools.

### Reason

A local tool isolates the tool-calling mechanism from external dependencies such as web search, network access, and source retrieval.

This allows us to verify that the agent can:

- receive a tool description
- decide when the tool is relevant
- invoke the tool
- use the returned information in its final response

Once this mechanism is verified, external research tools can be introduced with fewer variables involved in debugging.

### Status

Accepted