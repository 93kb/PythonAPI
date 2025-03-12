#FastAPIからGeminiAPIを呼び出したい

import requests #HTTPリクエストを送るためのライブラリ
from fastapi import FastAPI
import  json #JSONデータを送るためのライブラリ

# FastAPIのインスタンスを作成
app = FastAPI()

#APIを変数に格納
url ="https://www.dsk-cloud.com/blog/gemini-api"

# リクエストを送信
response = requests.get(url)

@app.get("/")
async def get_main():
    return {}


