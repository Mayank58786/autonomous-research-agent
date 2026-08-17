import asyncio

import app.config
from agents import Runner

from app.agents.manager import manager_agent


async def main():
    result = await Runner.run(
        manager_agent,
        "What are the best open-source LLMs for local development in 2026?",
    )

    print(result.final_output)


if __name__ == "__main__":
    asyncio.run(main())