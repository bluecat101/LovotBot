import os
from dotenv import load_dotenv


load_dotenv()

SLACK_API_TOKEN  = os.getenv("SLACK_API_TOKEN")