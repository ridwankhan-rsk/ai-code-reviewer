import os
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException

load_dotenv()
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from app.services.github_service import GitHubService

app = FastAPI(title="AI Code Reviewer", version="0.1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_methods=["*"],
    allow_headers=["*"],
)


class ReviewRequest(BaseModel):
    owner: str
    repo: str
    pr_number: int


class DiffRequest(BaseModel):
    diff: str


class GithubPRRequest(BaseModel):
    owner: str
    repo: str
    pull_number: int


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/api/reviews/")
def create_review(request: ReviewRequest):
    # stub — replace with real pipeline later
    return {
        "id": "stub-001",
        "owner": request.owner,
        "repo": request.repo,
        "pr_number": request.pr_number,
        "summary": "Stub summary — LLM not wired yet.",
        "risk_flags": [],
        "review_comments": [],
        "test_suggestions": [],
    }


@app.get("/api/reviews/")
def list_reviews():
    return []


@app.post("/api/review/github-pr")
async def review_github_pr(request: GithubPRRequest):
    token = os.getenv("GITHUB_TOKEN")
    if not token:
        raise HTTPException(status_code=500, detail="GITHUB_TOKEN not set")

    github = GitHubService(token)
    files = await github.get_pr_files(request.owner, request.repo, request.pull_number)
    return {
        "owner": request.owner,
        "repo": request.repo,
        "pull_number": request.pull_number,
        "files": files,
    }


@app.post("/api/review/diff")
def analyze_diff(request: DiffRequest):
    # stub — replace with real LLM call later
    return {
        "summary": "Stub: diff received and ready for analysis.",
        "risk_flags": [],
        "review_comments": [],
        "test_suggestions": [],
        "diff_length": len(request.diff),
    }
