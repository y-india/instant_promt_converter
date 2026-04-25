from fastapi import FastAPI
from pydantic import BaseModel
from groq import Groq
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # allow all (safe for local use)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


client = Groq(api_key="")  # set your Groq API key here


class TextRequest(BaseModel):
    text: str


def improve_prompt(text):
    instruction = f"""
You are a prompt editor.

Your task is to rewrite ONLY the given user prompt to improve clarity, precision, and structure.

Strict rules:
- Do NOT answer the prompt
- Do NOT add explanations
- Do NOT include headings, notes, or extra text
- Do NOT change the intent
- Only improve wording, structure, and specificity
- Keep it suitable for a coder or corporate professional
- Limit response to 5 times the prompt words

User prompt:
{text}
"""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": instruction}]
    )

    return response.choices[0].message.content.strip()





@app.post("/process")
async def process(req: TextRequest):
    text = req.text

    print("Received:", text)

    improved = improve_prompt(text)

    # save to file ()
    with open("improved_prompts.txt", "a", encoding="utf-8") as f:
        f.write("\n---\n")
        f.write(improved)

    print("Saved:", improved)

    return {
        "status": "ok",
        "result": improved
    }