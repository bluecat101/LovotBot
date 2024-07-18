# 説明
Lovotがこけたときに通知をSlackに送ります。
cronでn分おきに自動実行させることを前提にしています。

# 作業履歴
2024/7/18 完成

# 各ファイルの説明
- config.py
    - .envの内容を読み取る設定ファイル
- convert_datetime.py
    - UTCとJSTを変換する関数。LOVOTのログデータがUTCであるためJSTに変換する
- last_fallen_event_lovot.log
    - ログデータを取得したときに最後がこけたログであれば、そのログを記録するファイル。最後にこけていない場合や助けた場合にはログをリセットする。
- lovot.py
    - LOVOTにログデータを取得しに行くファイル
- main.py
    - 実行されるファイル。今日の時刻やログデータを取得してその結果に応じてSlackに送るか等を決める
- slack.py
    - Slackに通知を流す関数。

# 使用時に必要な環境関数
- SLACK_API_TOKEN 
    - SlackのAPIキー(メッセージを送るためのトークン)
- SLACK_CHANNEL
    - Slackのチャンネル(メッセージを送るチャンネル)
- LOVOT_API_KEY
    - LOVOTのAPIキー(ログデータを取得するためのAPI)
- LOVOT_GHOST_ID
    - LOVOTの個体ID
- LOVOT_ACCESS_URL_STAGE
    - LOVOTのAPIのエンドポイント