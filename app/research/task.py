from dataclasses import dataclass


@dataclass
class ResearchTask:
    question: str
    context: str = ""

    def to_prompt(self) -> str:
        prompt = f"Research question:\n{self.question}"

        if self.context:
            prompt += f"\n\nContext:\n{self.context}"

        return prompt