import { useState } from "react";
import RepoInput from "../components/RepoInput";

export default function Home() {
  const [parsed, setParsed] = useState(null);

  function handleSubmit({ owner, repo, pull_number }) {
    setParsed({ owner, repo, pull_number });
    // TODO: call api.createReview(owner, repo, pull_number) and navigate to /review/:id
    console.log("Parsed:", { owner, repo, pull_number });
  }

  return (
    <main>
      <h1>AI Code Reviewer</h1>
      <RepoInput onSubmit={handleSubmit} />
      {parsed && (
        <pre>
          owner = {parsed.owner}{"\n"}
          repo = {parsed.repo}{"\n"}
          pull_number = {parsed.pull_number}
        </pre>
      )}
    </main>
  );
}
