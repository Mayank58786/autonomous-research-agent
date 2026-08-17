from dataclasses import dataclass, field


@dataclass
class ResearchPlan:
    objective: str
    research_questions: list[str] = field(default_factory=list)