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
        async with httpx.AsyncClient() as client:
            response = await client.get(
                f"{self.BASE_URL}/repos/{owner}/{repo}/pulls",
                headers=self._headers,
                params={"state": state},
            )
            response.raise_for_status()
            return response.json()

    async def get_pr_metadata(self, owner: str, repo: str, pr_number: int) -> dict:
        async with httpx.AsyncClient() as client:
            response = await client.get(
                f"{self.BASE_URL}/repos/{owner}/{repo}/pulls/{pr_number}",
                headers=self._headers,
            )
            response.raise_for_status()
            return response.json()

    async def get_pr_diff(self, owner: str, repo: str, pr_number: int) -> str:
        headers = {**self._headers, "Accept": "application/vnd.github.diff"}
        async with httpx.AsyncClient() as client:
            response = await client.get(
                f"{self.BASE_URL}/repos/{owner}/{repo}/pulls/{pr_number}",
                headers=headers,
            )
            response.raise_for_status()
            return response.text

    async def get_pr_files(self, owner: str, repo: str, pr_number: int) -> list[dict]:
        async with httpx.AsyncClient() as client:
            response = await client.get(
                f"{self.BASE_URL}/repos/{owner}/{repo}/pulls/{pr_number}/files",
                headers=self._headers,
            )
            response.raise_for_status()
            return [
                {
                    "filename": f["filename"],
                    "status": f["status"],
                    "additions": f["additions"],
                    "deletions": f["deletions"],
                    "changes": f["changes"],
                    "patch": f.get("patch", ""),
                    "raw_url": f["raw_url"],
                }
                for f in response.json()
            ]
