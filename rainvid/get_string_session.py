from pyrogram import Client
from dotenv import load_dotenv
from os import getenv
import asyncio

load_dotenv()

app_name = getenv('TELEGRAM_APP_NAME')
api_id = int(getenv('TELEGRAM_API_ID'))
api_hash = getenv('TELEGRAM_API_HASH')
bot_token = getenv('TELEGRAM_BOT_TOKEN')

print(api_id, api_hash, bot_token)

app = Client(
  app_name,
  api_id=api_id, api_hash=api_hash,
  bot_token=bot_token
)
app.start()
session_string = app.export_session_string()
print(session_string)
app.stop()
