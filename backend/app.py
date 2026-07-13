from analyzer import analyze_response
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from surf_client import SurfClient

app = FastAPI(
    title="SurfBench Cloud API",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
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

    result = client.chat(request.prompt)

    if result.get("success"):

        analysis = analyze_response(result["answer"])

        result["analysis"] = analysis

    return result