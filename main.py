import random
import requests

API_KEY = "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"

with open("topics.txt", "r", encoding="utf-8") as f:
    topics = f.readlines()

topic = random.choice(topics).strip()

prompt = f"""
Write a professional LinkedIn post about:
{topic}

Rules:
- Human tone
- Short paragraphs
- Strong hook
- Maximum 120 words
- End with a question
"""

response = requests.post(
    url="https://openrouter.ai/api/v1/chat/completions",
    headers={
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
    },
    json={
        "model": "openai/gpt-3.5-turbo",
        "messages": [
            {
                "role": "user",
                "content": prompt
            }
        ]
    }
)

print(response.text)
