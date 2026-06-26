# AI Code Reviewer

Automated GitHub PR analysis tool that fetches diffs and uses an LLM to produce:
- Review comments with inline suggestions
- Risk flags (security, breaking changes, test coverage gaps)
- Test generation for changed code
- Summary of what the PR does

## Structure

```
ai-code-reviewer/
├── backend/          # FastAPI service
│   ├── app/
│   │   ├── routes/   # HTTP endpoints
│   │   ├── services/ # GitHub, LLM, diff parsing, risk, test logic
│   │   ├── models/   # Pydantic schemas
│   │   └── storage/  # DB layer
│   └── tests/
└── frontend/         # React UI
    └── src/
        ├── pages/
        ├── components/
        └── api/
```

## Quickstart

```bash
# Backend
cd backend
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env   # fill in GITHUB_TOKEN and ANTHROPIC_API_KEY
uvicorn app.main:app --reload

# Frontend
cd frontend
npm install
npm run dev
```

## Environment Variables

| Variable | Description |
|---|---|
| `GITHUB_TOKEN` | Personal access token with `repo` scope |
| `ANTHROPIC_API_KEY` | API key for the LLM backend |
| `DATABASE_URL` | SQLite or Postgres connection string |
