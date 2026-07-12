from fastapi import FastAPI
from pydantic import BaseModel
from surf_client import SurfClient

app = FastAPI(
    title="SurfBench Cloud API",
    version="1.0.0"
)

client = SurfClient()


class PromptRequest(BaseModel):
    prompt: str


@app.get("/")
def home():
    return {
        "message": "Welcome to SurfBench Cloud 🚀"
    }


@app.post("/prompt")
def run_prompt(request: PromptRequest):
    return client.chat(request.prompt)