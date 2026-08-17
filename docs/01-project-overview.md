# 1. Project Overview

## 1.1 Purpose

This project aims to build an autonomous AI research system.

The purpose is both practical and educational: to create a functioning agentic AI system while documenting the reasoning behind its architecture, implementation choices, experiments, and limitations.

The project is intentionally developed incrementally. Each version should produce a working system before additional complexity is introduced.

## 1.2 What Are We Building?

The end goal is an agentic AI system, not simply a single AI agent.

An individual agent is a reasoning component that can receive instructions, reason about a task, and use tools.

The complete system may contain multiple specialized agents coordinated by an orchestrator.

The distinction used throughout this project is:

- **Agent** — an individual reasoning component.
- **Tool** — an external capability an agent can invoke.
- **Orchestrator** — coordinates agents and controls the overall workflow.
- **Agentic system** — the complete system capable of planning, acting, evaluating results, and iterating.

## 1.3 Research Problem

Given a research objective, the system should be able to determine what information is required, obtain that information using available tools, evaluate the evidence, identify gaps or contradictions, and produce a useful final result.

A key objective is to move beyond a simple:

`prompt → model → answer`

workflow toward:

`objective → plan → actions/tools → observations → evaluation → iteration → result`

## 1.4 Initial Scope

Version 1 will focus on:

- autonomous research planning
- web/tool usage
- specialized research roles
- synthesis of collected information
- verification of important findings
- iterative research when necessary
- structured final output

## 1.5 Explicitly Out of Scope for V1

The following will not be implemented initially:

- sophisticated long-term memory
- production-scale infrastructure
- multi-user support
- complex user interfaces
- scheduled research
- autonomous email/report distribution
- large-scale vector databases
- custom browser automation

These may be considered in later versions if they provide clear value.

## 1.6 Development Philosophy

The project will be developed incrementally.

Each major implementation step should:

1. produce a working result
2. be tested locally
3. be committed to Git
4. document important decisions
5. establish a stable foundation for the next step