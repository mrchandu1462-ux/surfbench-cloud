import os
import requests
from dotenv import load_dotenv

load_dotenv()

url = "https://api.asksurf.ai/gateway/v1/responses"

headers = {
    "Authorization": f"Bearer {os.getenv('SURF_API_KEY')}",
    "Content-Type": "application/json"
}

payload = {
    "model": "surf-2.0-instant",
    "input": "What is Python?"
}

response = requests.post(url, headers=headers, json=payload)

print("Status:", response.status_code)
print(response.json())