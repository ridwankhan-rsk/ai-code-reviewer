from fastapi import APIRouter, HTTPException

from app.models.schemas import ReviewRequest, ReviewResponse

router = APIRouter()


@router.post("/", response_model=ReviewResponse)
async def create_review(request: ReviewRequest):
    """Fetch a PR diff and run the full LLM analysis pipeline."""
    # TODO: call github_service → diff_parser → llm_service → risk_analyzer → test_generator
    raise HTTPException(status_code=501, detail="Not implemented")


@router.get("/{review_id}", response_model=ReviewResponse)
async def get_review(review_id: str):
    """Retrieve a previously stored review by ID."""
    # TODO: load from db
    raise HTTPException(status_code=501, detail="Not implemented")


@router.get("/")
async def list_reviews():
    """List all stored reviews."""
    # TODO: query db
    return []
