"""Parses unified diff text into structured file hunks."""
from dataclasses import dataclass, field


@dataclass
class Hunk:
    old_start: int
    new_start: int
    lines: list[str] = field(default_factory=list)


@dataclass
class FileDiff:
    filename: str
    status: str  # added | modified | deleted | renamed
    hunks: list[Hunk] = field(default_factory=list)
    additions: int = 0
    deletions: int = 0


def parse_diff(raw_diff: str) -> list[FileDiff]:
    """Parse a unified diff string into a list of FileDiff objects."""
    # TODO: implement unified diff parsing
    raise NotImplementedError


def diff_to_context_string(file_diffs: list[FileDiff], max_lines: int = 500) -> str:
    """Flatten parsed diffs into a plain string suitable for LLM prompts."""
    # TODO: truncate and format for prompt injection
    raise NotImplementedError
