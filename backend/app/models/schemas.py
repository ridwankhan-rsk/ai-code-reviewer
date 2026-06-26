from pydantic import BaseModel


class ReviewRequest(BaseModel):
    owner: str
    repo: str
    pr_number: int


class RiskFlagSchema(BaseModel):
    level: str
    category: str
    description: str
    file: str | None = None
    line: int | None = None


class ReviewCommentSchema(BaseModel):
    file: str
    line: int | None = None
    comment: str


class TestSuggestionSchema(BaseModel):
    filename: str
    test_code: str


class ReviewResponse(BaseModel):
    id: str
    owner: str
    repo: str
    pr_number: int
    summary: str
    risk_flags: list[RiskFlagSchema]
    review_comments: list[ReviewCommentSchema]
    test_suggestions: list[TestSuggestionSchema]
    created_at: str
