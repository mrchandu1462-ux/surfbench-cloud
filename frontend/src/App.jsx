import { useState } from "react";
import axios from "axios";
import "./App.css";

function App() {
  const [prompt, setPrompt] = useState("");
  const [answer, setAnswer] = useState("");
  const [latency, setLatency] = useState("");
  const [usage, setUsage] = useState(null);

  async function askSurf() {
    try {
      const response = await axios.post(
        "http://127.0.0.1:8000/prompt",
        {
          prompt: prompt,
        }
      );

      setAnswer(response.data.answer);
      setLatency(response.data.latency);
      setUsage(response.data.usage);
    } catch (error) {
      console.error(error);
      setAnswer("Error connecting to backend.");
      setLatency("");
      setUsage(null);
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
    </div>
  );
}

export default App;