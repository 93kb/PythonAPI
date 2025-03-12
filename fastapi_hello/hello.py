#FastAPIで「Hello World」を返してもらう練習　※参考https://qiita.com/fujine/items/1fe6a29180befb589854
#必要なライブラリをインポート
from fastapi import FastAPI

#FastAPIのインスタンスを作成
app = FastAPI()

'''
app = FastAPI()で、FastAPIのインスタンスを作成します。
このappオブジェクトが、APIの全てのエンドポイントや設定を管理する中心的な存在となります。
appという名前は慣例であり、変更可能です。
'''

#GETかつエンドポイント「'/'」で呼ばれる関数
@app.get("/")
async def get_hello():
    return{"message":"hello World"}

'''
@app.get("/")はデコレータです。
ここでは、root関数をGETメソッドのルートパス(/)に紐付けます。
つまり、ブラウザでhttp://127.0.0.1:8000/ にアクセスすると、root関数が実行されます。 

async def root():でroot関数を定義しています。
asyncキーワードは、この関数が非同期関数であることを示します。
非同期関数を使用することで複数のリクエストを効率的に処理でき、
特にI/Oバウンドな処理（データベースアクセス、外部API呼び出しなど）で効果を発揮します。

return {"message": "Hello World"}でAPIのレスポンスを定義します。
辞書を返すと、FastAPIは自動的にJSON形式に変換してクライアントに返送します。
'''