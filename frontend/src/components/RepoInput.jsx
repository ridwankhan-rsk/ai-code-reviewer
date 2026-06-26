export default function RepoInput({ onSubmit }) {
  // TODO: form with owner, repo, PR number fields
  return (
    <form onSubmit={(e) => { e.preventDefault(); onSubmit(); }}>
      <input name="owner" placeholder="owner" />
      <input name="repo" placeholder="repo" />
      <input name="pr_number" type="number" placeholder="PR #" />
      <button type="submit">Analyse PR</button>
    </form>
  );
}
