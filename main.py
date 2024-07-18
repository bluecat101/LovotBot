import convert_datetime
import lovot
import slack
import pandas as pd
import random

LOG_PATH = "last_fallen_event_lovot.log"
fallen_message = ["こけちゃったよ。助けてーー", "HELP"]
thanks_message = ["ありがとう", "助かったよー"]


# 今日の日付を取得(日本時間であるが、形がUTCであるため、前日の15時となる。)
start_time = convert_datetime.get_today_start_time()

# LOVOTにアクセスしてデータを取得する
data = lovot.request_get(start_time)

# 取得した期間が短すぎてeventの記録がない時は抜ける
if not("events" in data):
  exit()

# データの日付を日本時間に変更
event_data = convert_datetime.convert_json_for_JST(data["events"])
df = pd.DataFrame.from_dict(event_data)

last_event_log = event_data[-1]["event_name"]
print(df)
last_fallen_date = df[df["event_name"] == "FALLEN"]["time"].iloc[-1] if "FALLEN" in df["event_name"].values else None

# ログファイルの先頭行を取得する
with open(LOG_PATH, encoding="UTF-8") as f:
  # ログファイルが空なら空文字を返す。
  log_data = f.readlines()
  first_line = log_data[0].rstrip("\n")  if len(log_data) > 0 else ""

# 最後のLOGがFALLENで止まっていて、過去のFALLENでないときSlackに送信する
if last_event_log == "FALLEN" and event_data[-1]["time"] != first_line:
  # FALLENメッセージをSlackに送信する
  slack.send_slack_message(random.choice(fallen_message))
  # logを更新する
  with open(LOG_PATH, mode='w') as f:
    f.write(event_data[-1]["time"])
elif last_event_log != "FALLEN" and last_fallen_date == first_line:
  # FALLEN状態から復帰した場合(第二条件式はSlackにFALLENメッセージを送って初めての復帰であるかのため)
  # THANKSメッセージをSlackに送信する
  slack.send_slack_message(random.choice(thanks_message))
  open(LOG_PATH, 'w').close()
elif last_event_log != "FALLEN":
  # 最後の状態がFALLENでない場合
  # logファイルの内容をクリアする
  open(LOG_PATH, 'w').close()
else:
  # FALLENメッセージでログが止まっていて、1度すでにSlackに送っている時
  exit()