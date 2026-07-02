import { useState } from "react";

export default function RepoInput({ onSubmit }) {
  const [repoUrl, setRepoUrl] = useState("");
  const [prNumber, setPrNumber] = useState("");
  const [error, setError] = useState("");

  function handleSubmit(e) {
    e.preventDefault();
    setError("");

    const match = repoUrl.match(/github\.com\/([^/]+)\/([^/]+)/);
    if (!match) {
      setError("Invalid GitHub URL. Expected: https://github.com/owner/repo");
      return;
    }

    const owner = match[1];
    const repo = match[2].replace(/\.git$/, "");
    const pull_number = parseInt(prNumber, 10);

    if (!pull_number) {
      setError("PR number must be a valid integer.");
      return;
    }

    onSubmit({ owner, repo, pull_number });
  }

  return (
    <form onSubmit={handleSubmit}>
      <div>
        <label>Repo URL</label>
        <input
          type="text"
          placeholder="https://github.com/owner/repo"
          value={repoUrl}
          onChange={(e) => setRepoUrl(e.target.value)}
        />
      </div>
      <div>
        <label>PR Number</label>
        <input
          type="number"
          placeholder="123"
          value={prNumber}
          onChange={(e) => setPrNumber(e.target.value)}
        />
      </div>
      {error && <p style={{ color: "red" }}>{error}</p>}
      <button type="submit">Analyze PR</button>
    </form>
  );
}
