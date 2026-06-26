export default function ReviewSummary({ summary = "" }) {
  // TODO: styled card with markdown rendering
  return <section><h2>Summary</h2><p>{summary || "No summary yet."}</p></section>;
}
