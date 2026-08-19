import asyncio

import app.config
from agents import Runner

from app.agents.manager import manager_agent
from app.research.context import ResearchContext
from app.research.state import ResearchState


async def main():
    question = "What are the main privacy advantages of running LLMs locally?"

    state = ResearchState(question=question)

    context = ResearchContext(
        question=question,
        state=state,
    )

    result = await Runner.run(
        manager_agent,
        context.to_prompt(),
        context=context,
    )

    print(result.final_output)

if __name__ == "__main__":
    asyncio.run(main())