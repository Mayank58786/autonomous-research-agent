from agents import Agent, WebSearchTool

from app.research.finding import ResearchFinding


search_agent = Agent(
    name="Research Searcher",
    model="gpt-5-mini",
    instructions="""
You are a research specialist.

Your job is to investigate a specific research question.

For each task:
1. Search for relevant information.
2. Prefer authoritative and primary sources.
3. Extract useful factual findings.
4. Include the source for each finding.
5. Focus only on the assigned research question.

Do not attempt to answer the overall user request.
Do not create a research plan.
Return concise, evidence-based findings.
""",
    tools=[
        WebSearchTool(),
    ],
    output_type=list[ResearchFinding],
)