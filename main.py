from fastapi import FastAPI, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware
from typing import Optional
import openai
import os

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Set your OpenAI API key (in Render, use Environment Variable)
openai.api_key = os.getenv("OPENAI_API_KEY")

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

    # Use OpenAI to generate answer
    try:
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful TA for the Tools in Data Science course."},
                {"role": "user", "content": question}
            ]
        )
        answer_text = completion.choices[0].message["content"]
    except Exception as e:
        answer_text = f"Error generating response: {str(e)}"

    return {
        "answer": answer_text,
        "image_info": image_info,
        "links": [
            {
                "url": "https://discourse.onlinedegree.iitm.ac.in/",
                "text": "Example reference link"
            }
        ]
    }
