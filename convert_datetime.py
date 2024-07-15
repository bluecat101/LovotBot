import datetime
import pytz


def convert_to_jst(utc_time_str):
  utc = pytz.utc
  jst = pytz.timezone('Asia/Tokyo')
  # タイムゾーン情報を付加
  utc_time = utc.localize(datetime.datetime.strptime(utc_time_str, '%Y-%m-%dT%H:%M:%SZ'))
  # 日本時間に変換
  jst_time = utc_time.astimezone(jst)
  # フォーマットを指定して文字列を返す
  return jst_time.strftime('%Y-%m-%d %H:%M:%S %Z')

def convert_json_for_JST(data):
  # 再帰的にJSON内の日付を変換する関数
  def convert_dates_in_json(data):
    if isinstance(data, dict):
      for key, value in data.items():
        if isinstance(value, str) and key == "time":
            data[key] = convert_to_jst(value)
        else:
            convert_dates_in_json(value)
    elif isinstance(data, list):
      for value in data:
        convert_dates_in_json(value)
  
  # JSONデータ内の日付を再帰的に一括変換
  convert_dates_in_json(data)
  return data




def get_today_start_time():
  # パラメータの値がutc時間で渡すので、今日-9時間(時差)で渡す。
  today_date_utc = datetime.datetime.now().replace(hour=0,minute=0,second=0,microsecond=0)
  time_difference = datetime.timedelta(hours=9)
  return (today_date_utc-time_difference).strftime('%Y-%m-%dT%H:%M:00Z')

