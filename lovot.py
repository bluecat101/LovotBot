import config
import datetime
import requests

## ---------- 初期設定 ---------- ##
# LOVOT用のAPIキーと個体ID
API_KEY  = config.API_KEY
GHOST_ID = config.GHOST_ID

# アクセス先
ACCESS_URL_STAGE = config.ACCESS_URL_STAGE


# APIを叩く
def request_get(type, start_time):
  # エンドポイント
  API_ENDPOINT = ACCESS_URL_STAGE.replace("GHOST_ID", GHOST_ID)
  
  # APIに送信する情報
  headers = {"accept": "application/json"}
  # 送信するURL
  url = f"{API_ENDPOINT}daily?start_time={start_time}&key={API_KEY}"

  # API接続の実行
  result = requests.get(url,headers=headers)
  
  # 整形して出力
  return result.json()


# パラメータの値がutc時間で渡すので、今日-9時間(時差)で渡す。
today_date_utc = datetime.datetime.now().replace(hour=0,minute=0,second=0,microsecond=0)
time_difference = datetime.timedelta(hours=9)
today_start_time = (today_date_utc-time_difference).strftime('%Y-%m-%dT%H:%M:00Z')

print(request_get(type, today_start_time))

