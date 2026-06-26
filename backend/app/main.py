from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes import review_routes, repo_routes
from app.storage.db import init_db

app = FastAPI(title="AI Code Reviewer", version="0.1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(review_routes.router, prefix="/api/reviews", tags=["reviews"])
app.include_router(repo_routes.router, prefix="/api/repos", tags=["repos"])


@app.on_event("startup")
async def startup():
    await init_db()


@app.get("/health")
async def health():
    return {"status": "ok"}
