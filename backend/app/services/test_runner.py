"""Executes generated tests in a sandboxed subprocess and captures output."""
import asyncio


async def run_tests(test_code: str, language: str = "python") -> dict:
    """
    Write test_code to a temp file, run the appropriate test runner,
    and return {passed, failed, output}.
    """
    # TODO: sandbox execution (docker or subprocess with timeout)
    raise NotImplementedError
