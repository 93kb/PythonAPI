#FastAPIからGeminiAPIを呼び出したい

import requests #HTTPリクエストを送るためのライブラリ
#import  json #JSONデータを送るためのライブラリ
from fastapi import FastAPI

url ="https://www.dsk-cloud.com/blog/gemini-api"

response = requests.get(url)

print(response.text)