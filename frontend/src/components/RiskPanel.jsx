export default function RiskPanel({ flags = [] }) {
  // TODO: colour-coded risk badges grouped by level
  return (
    <section>
      <h2>Risk Flags</h2>
      {flags.length === 0 ? <p>No risks detected.</p> : (
        <ul>{flags.map((f, i) => <li key={i}>[{f.level}] {f.category}: {f.description}</li>)}</ul>
      )}
    </section>
  );
}
