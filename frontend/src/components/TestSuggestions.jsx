export default function TestSuggestions({ suggestions = [] }) {
  // TODO: collapsible list of suggested tests per file
  return (
    <section>
      <h2>Test Suggestions</h2>
      {suggestions.map((s, i) => (
        <details key={i}>
          <summary>{s.filename}</summary>
          <pre>{s.test_code}</pre>
        </details>
      ))}
    </section>
  );
}
