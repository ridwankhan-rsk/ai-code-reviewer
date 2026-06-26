const BASE_URL = import.meta.env.VITE_API_URL ?? "http://localhost:8000/api";

async function request(path, options = {}) {
  const res = await fetch(`${BASE_URL}${path}`, {
    headers: { "Content-Type": "application/json", ...options.headers },
    ...options,
  });
  if (!res.ok) throw new Error(`API error ${res.status}: ${await res.text()}`);
  return res.json();
}

export const api = {
  createReview: (owner, repo, prNumber) =>
    request("/reviews/", {
      method: "POST",
      body: JSON.stringify({ owner, repo, pr_number: prNumber }),
    }),

  getReview: (reviewId) => request(`/reviews/${reviewId}`),

  listReviews: () => request("/reviews/"),

  listPRs: (owner, repo) => request(`/repos/${owner}/${repo}/pulls`),
};
