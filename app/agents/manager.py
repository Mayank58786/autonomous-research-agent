from agents import Agent

from app.research.plan import ResearchPlan


manager_agent = Agent(
    name="Research Manager",
    instructions="""
You are the Research Manager.

Your job is to analyze a user's research question and create
a clear research plan.

The plan should:
1. Define the overall research objective.
2. Break the objective into specific research questions.
3. Avoid performing the research itself.
""",
    output_type=ResearchPlan,
)
