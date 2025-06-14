from fastapi import FastAPI, UploadFile, File, Form # type: ignore
from typing import Optional
from fastapi.middleware.cors import CORSMiddleware # type: ignore

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.api_route("/api", methods=["POST", "GET", "OPTIONS"])
async def answer_question(
    question: Optional[str] = Form(None),
    image: Optional[UploadFile] = File(None)
):
    image_info = None
    if image:
        image_info = {
            "filename": image.filename,
            "content_type": image.content_type
        }

    if question:
        return {
            "answer": f"You asked: {question}",
            "image_info": image_info
        }
    else:
        # Respond with answer field even if no question
        return {
            "answer": "This endpoint supports POST requests with 'question' and optionally 'image'.",
            "image_info": None
        }
