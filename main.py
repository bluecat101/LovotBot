import convert_datetime
import lovot
import slack
import pandas as pd
import random

LOG_PATH = "last_help_event_lovot.log"
help_message = ["こけちゃったよ。助けてくれーー", "HELP", "起き上がれない"]
thanks_message = ["ありがとう", "助かったよー"]


# 今日の日付を取得(日本時間であるが、形がUTCであるため、前日の15時となる。)
start_time = convert_datetime.get_today_start_time()

# LOVOTにアクセスしてデータを取得する
data = lovot.request_get(type, start_time)
# 取得した期間が短すぎてeventの記録がない時は抜ける
if not("events" in data):
  exit()

# データの日付を日本時間に変更
event_data = convert_datetime.convert_json_for_JST(data["events"])
df = pd.DataFrame.from_dict(event_data)
last_help_date = df[df["event_name"] == "HELP"].tail()["time"]

# ログファイルの先頭行を取得する
with open(LOG_PATH, encoding="UTF-8") as f:
  # ログファイルが空なら空文字を返す。
  first_line = f.readlines()[0].rstrip("\n") if len(f.readlines()) > 1 else ""

# 最後のLOGがHELPで止まっていて、過去のHELPでないときSlackに送信する
if event_data[-1]["event_name"] == "HELP" and event_data[-1]["time"] != first_line:
  # HELPをSlackに送信する
  slack.send_slack_message(random.choice(help_message))
  # logを更新する
  with open(LOG_PATH, mode='w') as f:
    f.write(event_data[-1]["time"])
elif event_data[-1]["event_name"] != "HELP" and last_help_date == first_line:
  # HELP状態から復帰した場合(第二条件式はSlackにHELPメッセージを送って初めての復帰であるかのため)
  # HELPをSlackに送信する
  slack.send_slack_message(random.choice(thanks_message))
elif event_data[-1]["event_name"] != "HELP":
  # 最後の状態がHELPでない場合
  # logファイルの内容をクリアする
  open(LOG_PATH, 'w').close()

  