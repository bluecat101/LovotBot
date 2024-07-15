import config
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError


# SlackBot用のトークン
SLACK_API_TOKEN  = config.SLACK_API_TOKEN

def send_slack_message(text, channel = ""):
  # slack_token = os.environ["SLACK_API_TOKEN"]
  client = WebClient(token=SLACK_API_TOKEN)
  try:
    # chat.postMessage API を呼び出します
    response = client.chat_postMessage(
      channel = channel,
      text = text,
    )
  except SlackApiError as e:
    assert e.response["error"]

send_slack_message("slack bot test","#2024_2023-lovot")	
