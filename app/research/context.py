from dataclasses import dataclass

from app.research.state import ResearchState


@dataclass
class ResearchContext:
    question: str
    state: ResearchState

    def to_prompt(self) -> str:
        prompt = (
            f"Research question:\n{self.question}\n\n"
            f"Research objective:\n{self.state.objective}\n\n"
            f"Research questions:\n"
            + "\n".join(
                f"- {question}"
                for question in self.state.research_questions
            )
        )

        if self.state.findings:
            prompt += "\n\nFindings collected so far:\n"
            prompt += "\n".join(
                f"- {finding.statement} (Source: {finding.source})"
                for finding in self.state.findings
            )

        return prompt