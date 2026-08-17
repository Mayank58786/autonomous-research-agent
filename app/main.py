import asyncio

import app.config
from agents import Agent, Runner

from app.tools import get_project_status


agent = Agent(
    name="Research Agent",
    model="gpt-5-mini",
    instructions="""
    You are a research assistant.

    Provide accurate, concise answers.

    You have access to tools that provide information.
    Use a tool when it is relevant to answering the user's question.
    Do not invent information that a tool can provide.

    If you are uncertain about something, say so.
    """,
    tools=[get_project_status],
)


async def main():
    result = await Runner.run(
        agent,
        "What is the current development status of the Autonomous Research Agent project?"
    )

    print(result.final_output)


if __name__ == "__main__":
    asyncio.run(main())