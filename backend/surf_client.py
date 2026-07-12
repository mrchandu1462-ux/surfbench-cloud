import os
import time
import requests
from  dotenv import load_dotenv

load_dotenv()


class SurfClient:

    def __init__(self):

        self.api_key = os.getenv("SURF_API_KEY")

        if not self.api_key:
            raise ValueError("SURF_API_KEY not found in .env")

        self.url = "https://api.asksurf.ai/gateway/v1/responses"

        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

    def chat(self, prompt):

        payload = {
                 "model": "surf-2.0-instant",
                 "input": prompt
}

        start = time.perf_counter()

        response = requests.post(
            self.url,
            headers=self.headers,
            json=payload,
            timeout=120
        )

        latency = round(time.perf_counter() - start, 2)

        response.raise_for_status()

        data = response.json()

        return {
            "status_code": response.status_code,
            "latency": latency,
            "answer": data["output_text"],
            "usage": data.get("usage", {})
        }