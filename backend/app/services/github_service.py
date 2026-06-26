"""Fetches PR metadata and diffs from the GitHub API."""
import httpx


class GitHubService:
    BASE_URL = "https://api.github.com"

    def __init__(self, token: str):
        self._headers = {
            "Authorization": f"Bearer {token}",
            "Accept": "application/vnd.github.v3+json",
        }

    async def list_prs(self, owner: str, repo: str, state: str = "open") -> list[dict]:
        # TODO: GET /repos/{owner}/{repo}/pulls?state={state}
        raise NotImplementedError

    async def get_pr_metadata(self, owner: str, repo: str, pr_number: int) -> dict:
        # TODO: GET /repos/{owner}/{repo}/pulls/{pr_number}
        raise NotImplementedError

    async def get_pr_diff(self, owner: str, repo: str, pr_number: int) -> str:
        # TODO: GET /repos/{owner}/{repo}/pulls/{pr_number} with Accept: application/vnd.github.diff
        raise NotImplementedError

    async def get_pr_files(self, owner: str, repo: str, pr_number: int) -> list[dict]:
        # TODO: GET /repos/{owner}/{repo}/pulls/{pr_number}/files
        raise NotImplementedError
