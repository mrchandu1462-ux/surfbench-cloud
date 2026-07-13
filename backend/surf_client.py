import os
import time
import requests
from dotenv import load_dotenv

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

        try:
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
                "success": True,
                "status_code": response.status_code,
                "latency": latency,
                "answer": data.get("output_text", ""),
                "usage": data.get("usage", {})
            }

        except requests.exceptions.ReadTimeout:
            return {
                "success": False,
                "error": "Surf API timed out. Please try again.",
                "latency": None,
                "usage": {}
            }

        except requests.exceptions.HTTPError as e:
            return {
                "success": False,
                "error": f"HTTP Error: {e}",
                "latency": None,
                "usage": {}
            }

        except requests.exceptions.ConnectionError:
            return {
                "success": False,
                "error": "Unable to connect to the Surf API.",
                "latency": None,
                "usage": {}
            }

        except Exception as e:
            return {
                "success": False,
                "error": str(e),
                "latency": None,
                "usage": {}
            }