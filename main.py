from fastapi import FastAPI, UploadFile, File, Form
from typing import Optional
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/api")
async def answer_question(
    question: str = Form(...),
    image: Optional[UploadFile] = File(None)
):
    image_info = None
    if image:
        image_info = {
            "filename": image.filename,
            "content_type": image.content_type
        }

    return {
        "answer": f"You asked: {question}",
        "image_info": image_info,
        "links": [
            {
                "url": "https://discourse.onlinedegree.iitm.ac.in/",
                "text": "Example response link"
            }
        ]
    }
