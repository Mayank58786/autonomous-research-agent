import asyncio

import app.config
from agents import Agent, Runner, WebSearchTool


agent = Agent(
    name="Research Agent",
    model="gpt-5-mini",
    instructions="""
    You are a research assistant.

    Provide accurate, concise answers.

    You have access to web search.
    Use web search when the question requires current or external information.

    Prefer reliable and authoritative sources.
    Do not invent information.
    If sources disagree or information is uncertain, say so.
    """,
    tools=[
        WebSearchTool(),
    ],
)


async def main():
    result = await Runner.run(
        agent,
        "What are the most important recent developments in AI agents?"
    )

    print(result.final_output)


if __name__ == "__main__":
    asyncio.run(main())