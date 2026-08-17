from dataclasses import dataclass, field

from app.research.finding import ResearchFinding


@dataclass
class ResearchState:
    question: str
    objective: str = ""

    research_questions: list[str] = field(default_factory=list)

    sources: list[str] = field(default_factory=list)
    findings: list[ResearchFinding] = field(default_factory=list)
    unanswered_questions: list[str] = field(default_factory=list)

    status: str = "planning"