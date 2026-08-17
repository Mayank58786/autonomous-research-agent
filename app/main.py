import asyncio

from agents import Agent, Runner



agent = Agent(
    name="Research Agent",
    instructions="""
    You are a research assistant.

    Provide accurate, concise answers.
    If you are uncertain about something, say so.
    """,
)


async def main():
    result = await Runner.run(
        agent,
        "What is an AI agent?"
    )

    print(result.final_output)


if __name__ == "__main__":
    asyncio.run(main())
    