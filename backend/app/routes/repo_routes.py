from fastapi import APIRouter, HTTPException

router = APIRouter()


@router.get("/{owner}/{repo}/pulls")
async def list_pull_requests(owner: str, repo: str, state: str = "open"):
    """List pull requests for a GitHub repo."""
    # TODO: call github_service.list_prs(owner, repo, state)
    raise HTTPException(status_code=501, detail="Not implemented")


@router.get("/{owner}/{repo}/pulls/{pr_number}/diff")
async def get_pr_diff(owner: str, repo: str, pr_number: int):
    """Fetch the raw diff for a single PR."""
    # TODO: call github_service.get_pr_diff(owner, repo, pr_number)
    raise HTTPException(status_code=501, detail="Not implemented")
