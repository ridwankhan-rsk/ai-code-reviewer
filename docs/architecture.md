# Architecture

## Request flow

```
Browser → POST /api/reviews/
            │
            ├─ GitHubService    fetch PR diff
            ├─ DiffParser       structured hunks
            ├─ LLMService       summary + comments + test code
            ├─ RiskAnalyzer     flag security / breaking-change risks
            └─ TestGenerator    group tests by file
                    │
                    └─ store ReviewResponse in DB → return to client
```

## Components

| Layer | Technology |
|---|---|
| Backend API | FastAPI + uvicorn |
| LLM | Anthropic claude-sonnet-4-6 |
| GitHub API | httpx (async) |
| Storage | SQLAlchemy async + SQLite (dev) / Postgres (prod) |
| Frontend | React + Vite + react-router-dom |

## Key design decisions

- Diff context is truncated before being sent to the LLM to stay within token limits.
- All LLM calls are async; the review endpoint streams progress via SSE (planned).
- Test runner executes in a subprocess with a hard timeout to prevent hangs.
