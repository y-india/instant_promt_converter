import keyboard
import pyperclip
import time
from groq import Groq

client = Groq(api_key="")

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
- Limit response to 5times the prompt words

User prompt:
{text}
"""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": instruction}]
    )

    return response.choices[0].message.content.strip()


def process_selection():
    keyboard.press_and_release("ctrl+c")
    time.sleep(0.3)

    text = pyperclip.paste()
    if not text.strip():
        print("No text selected")
        return

    improved = improve_prompt(text)

    with open("improved_prompts.txt", "a", encoding="utf-8") as f:
        f.write("\n---\n")
        f.write(improved)

    print("Saved improved prompt")


keyboard.add_hotkey("ctrl+alt+space", process_selection)

print("Running... Press ctrl+alt+space")
keyboard.wait()

