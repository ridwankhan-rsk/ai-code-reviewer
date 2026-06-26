"""Wraps LLMService to produce and optionally persist test suggestions."""
from app.services.llm_service import LLMService


class TestGenerator:
    def __init__(self, llm: LLMService):
        self._llm = llm

    async def suggest_tests(self, diff_context: str) -> dict:
        """Return suggested tests grouped by file."""
        # TODO: call llm.generate_tests, parse into {filename: test_code} mapping
        raise NotImplementedError
