import { useState } from "react";
import axios from "axios";

function App() {
  const [prompt, setPrompt] = useState("");
  const [answer, setAnswer] = useState("");

  async function askSurf() {
    try {
      const response = await axios.post(
        "http://127.0.0.1:8000/prompt",
        {
          prompt: prompt,
        }
      );

      setAnswer(response.data.answer);
    } catch (error) {
      console.error(error);
      setAnswer("Error connecting to backend.");
    }
  }

  return (
    <div>
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

      <hr />

      <h2>Response</h2>

      <p>{answer}</p>
    </div>
  );
}

export default App;