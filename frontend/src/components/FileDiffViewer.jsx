export default function FileDiffViewer({ comments = [] }) {
  // TODO: render diff hunks with syntax highlighting and inline comments
  return <section><h2>Diff & Comments</h2><pre>{JSON.stringify(comments, null, 2)}</pre></section>;
}
