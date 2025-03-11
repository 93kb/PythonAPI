# APIレスポンス確認・練習　※参考https://www.sejuku.net/blog/7360

# requestsライブラリをインポート
import requests

# APIリクエストの送信先URL
api_url = "https://api.open-meteo.com/v1/forecast?latitude=35.6895&longitude=139.6917&hourly=temperature_2m&timezone=Asia/Tokyo"

# リクエストを送信
response = requests.get(api_url)

# ステータスコードを確認し、データを表示
if response.status_code == 200:
    data = response.json()  # JSON形式に変換

    # APIレスポンスから最新の気温を取得
    latest_temperature = data['hourly']['temperature_2m'][0]

    # 気温を表示
    print(f'現在の気温は{latest_temperature}℃です。')
else:
    print(f"データ取得に失敗しました。{response.status_code}")