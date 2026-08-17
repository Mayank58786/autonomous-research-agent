import asyncio

import app.config
from agents import Agent, Runner


agent = Agent(
    name="Research Agent",
    model="gpt-5-mini",
    instructions="""
    You are a research assistant.

    Provide accurate, concise answers.
    If you are uncertain about something, say so.
    """,
)


async def main():
    result = await Runner.run(
        agent,
        "What is an AI agent? Answer in three sentences."
    )

    print(result.final_output)


if __name__ == "__main__":
    asyncio.run(main())