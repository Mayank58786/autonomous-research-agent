import app.config

from agents import Runner

from app.agents.manager import manager_agent
from app.research.plan import ResearchPlan
from app.research.state import ResearchState


def apply_plan(
    state: ResearchState,
    plan: ResearchPlan,
) -> ResearchState:
    state.objective = plan.objective
    state.research_questions = plan.research_questions
    state.status = "researching"

    return state


async def create_research_state(question: str) -> ResearchState:
    result = await Runner.run(
        manager_agent,
        question,
    )

    plan: ResearchPlan = result.final_output

    state = ResearchState(question=question)

    return apply_plan(state, plan)