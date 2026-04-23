import pyperclip
import keyboard
import time
from groq import Groq

# Initialize client
client = Groq(api_key="")



def test_clipboard_to_llm():
    
    text = pyperclip.paste()

    if not text.strip():
        print("Clipboard is empty. First copy text using Ctrl+C, then press shortcut.")
        return

    print("\n--- Clipboard Content ---")
    print(text)

    instruction = f"""
Before answering write the exact promt that was given to you below. 

Prompt:
{text}
"""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": instruction}]
    )

    output = response.choices[0].message.content.strip()

    print("\n--- LLM Output ---")
    print(output)


# Register shortcut
keyboard.add_hotkey("alt+ctrl+space", test_clipboard_to_llm)

print("Running...")
print("Step 1: Select text and press Ctrl+C")
print("Step 2: Press alt+ctrl+space")

keyboard.wait()

# OUTPUT:

# Clipboard is empty
# Clipboard is empty
