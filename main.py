#FastAPIからGeminiAPIを呼び出したい

import requests #HTTPリクエストを送るためのライブラリ
from fastapi import FastAPI
import  json #JSONデータを送るためのライブラリ
from google import genai

# FastAPIのインスタンスを作成
app = FastAPI()

#APIを変数に格納
url ="https://gemini.google.com/app?hl=ja"

client = genai.Client(api_key="YOUR_API_KEY")

# リクエストを送信
response = requests.get()

@app.get("/")
async def get_main(contents:str):
    response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents="Explain how AI works"
)

    return response.json

print(response.text)