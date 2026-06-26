import { BrowserRouter, Routes, Route } from "react-router-dom";
import Home from "./pages/Home";
import ReviewPage from "./pages/ReviewPage";

export default function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/review/:reviewId" element={<ReviewPage />} />
      </Routes>
    </BrowserRouter>
  );
}
