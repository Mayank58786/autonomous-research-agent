import asyncio

from app.research.orchestrator import create_research_state


async def main():
    state = await create_research_state(
        "What are the best open-source LLMs for local development in 2026?"
    )

    print(state)


if __name__ == "__main__":
    asyncio.run(main())