from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
import openai
import os

app = FastAPI()
openai.api_key = os.environ.get("OPENAI_API_KEY")

class StudentQuery(BaseModel):
    question: str
    image: Optional[str] = None  # base64 string (optional)

@app.post("/api/")
async def virtual_ta(query: StudentQuery):
    messages = [{"type": "text", "text": query.question}]

    if query.image:
        messages.append({
            "type": "image_url",
            "image_url": {
                "url": f"data:image/png;base64,{query.image}"
            },
            "detail": "low"
        })

    response = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": messages}]
    )

    answer = response["choices"][0]["message"]["content"]

    # Hardcoded example links (you can add scraping later)
    links = [
        {
            "url": "https://discourse.onlinedegree.iitm.ac.in/t/ga5-question-8-clarification/155939/4",
            "text": "Use the model that’s mentioned in the question."
        },
        {
            "url": "https://discourse.onlinedegree.iitm.ac.in/t/ga5-question-8-clarification/155939/3",
            "text": "Use a tokenizer to get the number of tokens."
        }
    ]

    return {"answer": answer, "links": links}
