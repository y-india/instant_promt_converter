from groq import Groq

from groq import Groq

client = Groq(api_key="")

response = client.chat.completions.create(
    model="llama-3.1-8b-instant",
    messages=[
        {"role": "user", "content": "Explain CUET exam process simply"}
    ]
)

print(response.choices[0].message.content)



# import requests
# import os

# api_key = ""

# url = "https://api.groq.com/openai/v1/models"


# headers = {
#     "Authorization": f"Bearer {api_key}",
#     "Content-Type": "application/json"
# }


# response = requests.get(url, headers=headers)

# print(response.json())



