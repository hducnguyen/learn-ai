API_KEY = "AIzaSyBj-V0yJ0fxgpyi23MhVr4yymGEmxeQx8A"

import requests
import json

URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-latest:generateContent?key={API_KEY}"
while True:
    user_input = input("User: ")
    response = requests.post(URL, json={"contents":[{"parts":[{"text":user_input}]}]}, headers={'Content-Type': 'application/json'})
    data = response.json()
    text = data["candidates"][0]["content"]["parts"][0]["text"]
    print("\nBot: ",text)