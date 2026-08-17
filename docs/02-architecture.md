# 2. Architecture

## 2.1 Initial Concept

The system is designed as a coordinated agentic research workflow.

At a high level:

User
↓
Orchestrator
↓
Research / Analysis Agents
↓
Tools
↓
Evidence
↓
Synthesis
↓
Verification
↓
Final Result

## 2.2 Core Components

### Orchestrator

The orchestrator is responsible for managing the overall research objective.

It determines what work is required, coordinates specialized agents, and controls the overall workflow.

### Research Agents

Specialized agents perform focused research tasks.

Different agents may eventually be responsible for areas such as:

- information discovery
- source analysis
- comparative analysis
- fact verification

### Tools

Tools provide capabilities that the language model does not inherently possess.

Examples include:

- web search
- webpage retrieval
- document processing
- calculations
- other external APIs

Tool usage is a fundamental part of the agentic design.

### Synthesizer

The synthesizer combines the collected evidence into a coherent research result.

### Verifier

The verifier evaluates important claims and attempts to identify unsupported, contradictory, or unreliable conclusions.

## 2.3 Intended Control Loop

The intended V1 workflow is:

Research objective
↓
Research planning
↓
Information gathering
↓
Evidence synthesis
↓
Verification
↓
Decision:
- sufficient evidence → final result
- insufficient evidence → additional research
↓
Final result

The iterative branch is an important part of the autonomous behavior of the system.

## 2.4 Architecture Evolution

This document will be updated as implementation reveals limitations in the initial architecture.

The architecture is therefore considered a working design rather than a fixed specification.