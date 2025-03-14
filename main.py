#FastAPIからGeminiAPIを呼び出したい

from fastapi import FastAPI
from google import genai
from pydantic import BaseModel

# FastAPIのインスタンスを作成
app = FastAPI()

class Item(BaseModel):
    contents: str

@app.post("/")

async def get_main(item: Item):
    
    #APIを変数に格納
    client = genai.Client(api_key="YOUR_API_KEY") #取得したAPIキーを設定する

    try:
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=item.contents
        )

    except:
        return "error"

    return response