import pyperclip
import keyboard
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
- Limit response to 5 times the prompt words

User prompt:
{text}
"""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": instruction}]
    )

    return response.choices[0].message.content.strip()


def process_selection():
    text = pyperclip.paste()

    if not text.strip():
        print("Clipboard is empty. First press Ctrl+C on selected text, then use shortcut.")
        return

    improved = improve_prompt(text)

    with open("improved_prompts.txt", "a", encoding="utf-8") as f:
        f.write("\n---\n")
        f.write(improved)

    print("Saved improved prompt")


keyboard.add_hotkey("ctrl+alt+space", process_selection)

print("Running...")
print("Step 1: Select text and press Ctrl+C")
print("Step 2: Press ctrl+alt+space")

keyboard.wait()