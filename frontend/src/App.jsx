import { useState } from "react";
import axios from "axios";
import "./App.css";

function App() {
  const [prompt, setPrompt] = useState("");
  const [answer, setAnswer] = useState("");
  const [latency, setLatency] = useState("");
  const [usage, setUsage] = useState(null);
  const [analysis, setAnalysis] = useState(null);

  async function askSurf() {
    try {
      const response = await axios.post(
        "http://127.0.0.1:8000/prompt",
        {
          prompt: prompt,
        }
      );

      // Debug Logs
      console.log("========== API RESPONSE ==========");
      console.log("Full Response:", response.data);
      console.log("Answer:", response.data.answer);
      console.log("Usage:", response.data.usage);
      console.log("Analysis:", response.data.analysis);
      console.log("==================================");

      setAnswer(response.data.answer);
      setLatency(response.data.latency);
      setUsage(response.data.usage);
      setAnalysis(response.data.analysis);

    } catch (error) {
      console.error("Backend Error:", error);

      setAnswer("Error connecting to backend.");
      setLatency("");
      setUsage(null);
      setAnalysis(null);
    }
  }

  return (
    <div className="container">
      <h1>🚀 SurfBench Cloud</h1>

      <p>Powered by Surf AI</p>

      <textarea
        rows="8"
        cols="60"
        placeholder="Ask anything..."
        value={prompt}
        onChange={(e) => setPrompt(e.target.value)}
      />

      <br />
      <br />

      <button onClick={askSurf}>Ask Surf</button>

      {usage && (
        <div className="metrics">
          <p>⏱️ Latency: {latency} s</p>
          <p>📥 Input Tokens: {usage.input_tokens}</p>
          <p>📤 Output Tokens: {usage.output_tokens}</p>
          <p>🔢 Total Tokens: {usage.total_tokens}</p>
        </div>
      )}

      <h2>Response</h2>

      <div className="response-card">
        {answer || "Your Surf AI response will appear here..."}
      </div>

      <hr />

      <h2>Verification Report</h2>

      {analysis ? (
        <div className="analysis-card">
          <p>
            <strong>Score:</strong> {analysis.score}/100
          </p>

          <p>
            <strong>Language:</strong> {analysis.language}
          </p>

          <h3>✅ Passed</h3>
          <ul>
            {analysis.passed?.map((item, index) => (
              <li key={index}>{item}</li>
            ))}
          </ul>

          <h3>⚠ Warnings</h3>
          <ul>
            {analysis.warnings?.map((item, index) => (
              <li key={index}>{item}</li>
            ))}
          </ul>

          <h3>💡 Suggestions</h3>
          <ul>
            {analysis.suggestions?.map((item, index) => (
              <li key={index}>{item}</li>
            ))}
          </ul>
        </div>
      ) : (
        <div className="analysis-card">
          <p>No analysis received from backend.</p>
        </div>
      )}
    </div>
  );
}

export default App;