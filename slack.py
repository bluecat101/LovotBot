import config
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError


# SlackBot用のトークンとチャンネル
SLACK_API_TOKEN  = config.SLACK_API_TOKEN
SLACK_CHANNEL  = config.SLACK_CHANNEL


def send_slack_message(text):
  client = WebClient(token=SLACK_API_TOKEN)
  
  try:
    # chat.postMessage API を呼び出します
    response = client.chat_postMessage(
      channel = SLACK_CHANNEL,
      text = text,
    )
  except SlackApiError as e:
    assert e.response["error"]
