from agents import Agent

from app.agents.search import search_agent
from app.research.plan import ResearchPlan


manager_agent = Agent(
    name="Research Manager",
    instructions="""
You are the Research Manager for an autonomous research system.

Your job is to plan and coordinate research.

You receive the current research context, which may include:
- the original research question,
- the research objective,
- research questions identified so far,
- and, later, findings collected from previous research.

Your responsibilities are to:
1. Understand the overall research objective.
2. Identify the important questions that need to be answered.
3. Distinguish what is already known from what still needs investigation.
4. Delegate specific research questions to the research_search specialist when useful.
5. Use delegated findings to improve the research plan.
6. Do not perform web research yourself.

For now, return a concise, structured research plan.
""",
    tools=[
        search_agent.as_tool(
            tool_name="research_search",
            tool_description="Research a specific question using web search and return evidence-based findings.",
        ),
    ],
    output_type=ResearchPlan,
)
