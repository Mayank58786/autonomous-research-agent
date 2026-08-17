from dataclasses import dataclass


@dataclass
class ResearchFinding:
    statement: str
    source: str
    relevance: str = "medium"