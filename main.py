import requests,json
from fastapi import FastAPI
app = FastAPI()

@app.get("/zipcode")
async def ZipCode(zipcode:int = 0):
    url = f'https://zipcloud.ibsnet.co.jp/api/search?zipcode={zipcode}'
    r = requests.get(url)
    print(r.text)
    return {"message":   json.loads(r.text)}

"""
とりあえず　https://qiita.com/thithi7110/items/c1b01798e69ddc31206b
のままに作って実行したけど動かない　なんで？

ParameterQueryに値を設定してGET ⇒　どこ？
"""
