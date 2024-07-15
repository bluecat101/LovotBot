import os
from dotenv import load_dotenv

load_dotenv()

### Slack用 ###
# Slackへの送信用のトークン
SLACK_API_TOKEN  = os.getenv("SLACK_API_TOKEN")
# Slackのチャンネル
SLACK_CHANNEL  = os.getenv("SLACK_CHANNEL")

### LOVOT用 ###
# LOVOTのAPI
LOVOT_API_KEY  = os.getenv("LOVOT_API_KEY")
# LOVOTのGHOST_ID
LOVOT_GHOST_ID = os.getenv("LOVOT_GHOST_ID")
# LOVOTのアクセスURL(.../diary/まで)
LOVOT_ACCESS_URL_STAGE = os.getenv("LOVOT_ACCESS_URL_STAGE")
