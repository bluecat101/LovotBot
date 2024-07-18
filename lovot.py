import config
import datetime
import requests

## ---------- 初期設定 ---------- ##
# LOVOT用のAPIキーと個体ID
LOVOT_API_KEY  = config.LOVOT_API_KEY
LOVOT_GHOST_ID = config.LOVOT_GHOST_ID

# アクセス先
LOVOT_ACCESS_URL_STAGE = config.LOVOT_ACCESS_URL_STAGE


# APIを叩く
def request_get(start_time):
  # エンドポイント
  API_ENDPOINT = LOVOT_ACCESS_URL_STAGE.replace("GHOST_ID", LOVOT_GHOST_ID)
  
  # APIに送信する情報
  headers = {"accept": "application/json"}
  # 送信するURL
  url = f"{API_ENDPOINT}daily?start_time={start_time}&key={LOVOT_API_KEY}"

  # API接続の実行
  result = requests.get(url,headers=headers)
  
  # 整形して出力
  return result.json()

