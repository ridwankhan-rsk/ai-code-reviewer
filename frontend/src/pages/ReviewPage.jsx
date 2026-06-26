import { useParams } from "react-router-dom";
import ReviewSummary from "../components/ReviewSummary";
import RiskPanel from "../components/RiskPanel";
import FileDiffViewer from "../components/FileDiffViewer";
import TestSuggestions from "../components/TestSuggestions";
import GeneratedTests from "../components/GeneratedTests";
import TestRunOutput from "../components/TestRunOutput";

export default function ReviewPage() {
  const { reviewId } = useParams();
  // TODO: fetch review data via api.getReview(reviewId)
  const review = null;

  if (!review) return <p>Loading review {reviewId}…</p>;

  return (
    <main>
      <ReviewSummary summary={review.summary} />
      <RiskPanel flags={review.risk_flags} />
      <FileDiffViewer comments={review.review_comments} />
      <TestSuggestions suggestions={review.test_suggestions} />
      <GeneratedTests />
      <TestRunOutput />
    </main>
  );
}
