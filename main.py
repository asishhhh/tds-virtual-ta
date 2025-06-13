from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class StudentQuery(BaseModel):
    question: str
    image: Optional[str] = None

@app.post("/api/")
async def virtual_ta(query: StudentQuery):
    return {
        "answer": "This is a test response.",
        "links": [
            {"url": "https://example.com/1", "text": "Example Link 1"},
            {"url": "https://example.com/2", "text": "Example Link 2"}
        ]
    }
