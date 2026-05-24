import random
import requests

API_KEY = "AIzaSyDy4mNJKNsm-FiQIhLiR6iucWYPc0Y8K6w"

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

url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash-exp:generateContent?key={API_KEY}"

data = {
    "contents": [
        {
            "parts": [
                {
                    "text": prompt
                }
            ]
        }
    ]
}

response = requests.post(url, json=data)

print(response.text)
