import os
from dotenv import load_dotenv

load_dotenv()

# Slack用
SLACK_API_TOKEN  = os.getenv("SLACK_API_TOKEN")

# LOVOT用
API_KEY  = os.getenv("API_KEY")
GHOST_ID = os.getenv("GHOST_ID")
ACCESS_URL_STAGE = os.getenv("ACCESS_URL_STAGE")
