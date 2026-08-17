import asyncio

import app.config
from agents import Runner

from app.agents.search import search_agent
from app.research.task import ResearchTask


async def main():
    task = ResearchTask(
        question="What are the main advantages of running an LLM locally?",
        context="Focus on privacy, latency, cost, and developer control.",
    )

    result = await Runner.run(
        search_agent,
        task.to_prompt(),
    )

    print(result.final_output)


if __name__ == "__main__":
    asyncio.run(main())