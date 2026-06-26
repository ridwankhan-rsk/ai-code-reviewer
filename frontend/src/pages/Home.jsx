import RepoInput from "../components/RepoInput";

export default function Home() {
  // TODO: on submit, call api.createReview and navigate to /review/:id
  return (
    <main>
      <h1>AI Code Reviewer</h1>
      <RepoInput onSubmit={() => {}} />
    </main>
  );
}
