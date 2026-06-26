"""Derives risk flags from the LLM review and parsed diff."""
from dataclasses import dataclass
from enum import Enum


class RiskLevel(str, Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"


@dataclass
class RiskFlag:
    level: RiskLevel
    category: str   # e.g. "security", "breaking-change", "test-coverage"
    description: str
    file: str | None = None
    line: int | None = None


def analyze_risks(diff_context: str, review_comments: list[dict]) -> list[RiskFlag]:
    """Produce a list of RiskFlag objects for the PR."""
    # TODO: heuristic rules + LLM-assisted classification
    raise NotImplementedError
