# Demo Script

1. Start backend: `cd backend && uvicorn app.main:app --reload`
2. Start frontend: `cd frontend && npm run dev`
3. Open `http://localhost:5173`
4. Enter a public repo owner/name and a PR number, click **Analyse PR**
5. The review page shows:
   - Plain-English summary of the PR
   - Risk flags (colour-coded by severity)
   - Inline review comments mapped to the diff
   - Generated test stubs for changed code
   - (Optional) Run generated tests and see pass/fail output
