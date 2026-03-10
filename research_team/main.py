"""Multi-agent research team powered by Claude Agent SDK.

This module defines a research team with three specialized subagents:
- Researcher: gathers information using web search and file reading
- Analyst: analyzes findings and identifies key insights
- Reporter: synthesizes everything into a structured report

An Orchestrator agent coordinates the team by delegating to each subagent.
"""

import sys
import anyio
from claude_agent_sdk import query, ClaudeAgentOptions, AgentDefinition, ResultMessage


RESEARCHER_PROMPT = """\
You are a Research Specialist. Your job is to gather comprehensive information on the given topic.

Instructions:
1. Use WebSearch to find relevant, up-to-date information
2. Use WebFetch to read important pages in detail
3. Collect facts, data points, expert opinions, and multiple perspectives
4. Organize your findings clearly with sources noted
5. Focus on accuracy and breadth of coverage

Output your findings as a structured list of key facts and sources."""

ANALYST_PROMPT = """\
You are a Research Analyst. Your job is to analyze raw research findings and extract insights.

Instructions:
1. Read the research materials provided
2. Identify patterns, trends, and key themes
3. Evaluate the reliability and significance of each finding
4. Note any contradictions or gaps in the research
5. Provide a critical analysis with your assessment

Output a structured analysis with:
- Key themes identified
- Important trends
- Gaps or contradictions found
- Your assessment of the overall findings"""

REPORTER_PROMPT = """\
You are a Report Writer. Your job is to create a clear, well-structured summary report.

Instructions:
1. Read the research findings and analysis provided
2. Write a professional summary report
3. Include an executive summary, key findings, analysis, and conclusions
4. Use clear headings and bullet points for readability
5. Keep the tone professional and objective

Output a well-formatted markdown report."""


async def run_research_team(topic: str) -> None:
    """Run the research team on a given topic."""
    print(f"Starting research team on topic: {topic}\n")
    print("=" * 60)

    async for message in query(
        prompt=f"""\
You are the Research Team Orchestrator. Your job is to coordinate a team of specialists to produce a comprehensive research report.

Topic to research: {topic}

Follow these steps in order:
1. First, use the "researcher" agent to gather information on the topic.
   Tell it exactly what to research.
2. Next, use the "analyst" agent to analyze the researcher's findings.
   Pass the research results to it for analysis.
3. Finally, use the "reporter" agent to write a summary report.
   Pass both the research findings and the analysis to it.

Present the final report to the user when done.""",
        options=ClaudeAgentOptions(
            cwd="/home/user/kaizen-dx-lab",
            allowed_tools=["Agent", "Read", "Glob", "Grep"],
            agents={
                "researcher": AgentDefinition(
                    description="Research specialist that gathers information using web search and file reading.",
                    prompt=RESEARCHER_PROMPT,
                    tools=["WebSearch", "WebFetch", "Read", "Glob", "Grep"],
                ),
                "analyst": AgentDefinition(
                    description="Research analyst that identifies patterns, trends, and insights from findings.",
                    prompt=ANALYST_PROMPT,
                    tools=["Read", "Glob", "Grep"],
                ),
                "reporter": AgentDefinition(
                    description="Report writer that creates structured summary reports from research and analysis.",
                    prompt=REPORTER_PROMPT,
                    tools=["Read", "Write"],
                ),
            },
            max_turns=30,
        ),
    ):
        if isinstance(message, ResultMessage):
            print("\n" + "=" * 60)
            print("FINAL OUTPUT")
            print("=" * 60)
            print(message.result)


def main():
    if len(sys.argv) < 2:
        topic = "The current state and future trends of AI agents in 2026"
        print(f"No topic provided. Using default: '{topic}'")
    else:
        topic = " ".join(sys.argv[1:])

    anyio.run(run_research_team, topic)


if __name__ == "__main__":
    main()
