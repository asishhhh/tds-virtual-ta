from fastapi import FastAPI, UploadFile, File, Form
from typing import Optional
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods: POST, GET, OPTIONS, etc.
    allow_headers=["*"],  # Allow all headers
)

@app.api_route("/api", methods=["POST", "GET", "OPTIONS"])
async def answer_question(
    question: str = Form(None),
    image: Optional[UploadFile] = File(None)
):
    # For GET requests, just return an info message
    if question is None:
        return {"message": "This endpoint supports POST requests with 'question' and optionally 'image'."}

    image_info = None
    if image:
        image_info = {
            "filename": image.filename,
            "content_type": image.content_type
        }

    return {
        "answer": f"You asked: {question}",
        "image_info": image_info
    }
