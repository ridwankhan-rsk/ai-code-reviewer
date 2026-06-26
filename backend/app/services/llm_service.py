"""Calls the Anthropic API to analyse a PR diff."""
import anthropic


class LLMService:
    MODEL = "claude-sonnet-4-6"

    def __init__(self, api_key: str):
        self._client = anthropic.AsyncAnthropic(api_key=api_key)

    async def summarize(self, diff_context: str) -> str:
        """Return a plain-English summary of what the PR changes."""
        # TODO: build prompt and call self._client.messages.create(...)
        raise NotImplementedError

    async def review_comments(self, diff_context: str) -> list[dict]:
        """Return structured inline review comments for the diff."""
        # TODO: prompt → parse JSON array of {file, line, comment}
        raise NotImplementedError

    async def generate_tests(self, diff_context: str) -> str:
        """Return suggested unit tests for the changed code."""
        # TODO: prompt → return raw test code string
        raise NotImplementedError
