from pyrogram import Client 
from pyrogram.types import Message
from dotenv import load_dotenv
from os import getenv
import random

load_dotenv()

class Telegram:
  def __init__(self):
    self.app_name = getenv('TELEGRAM_APP_NAME')
    self.message_ids_file_path = './messageIds.txt'
    self.string_session = getenv('TELEGRAM_STRING_SESSION')
    self.base_chat_id = int(getenv('TELEGRAM_BASE_CHAT_ID'))
    self.log_chat_id = int(getenv('TELEGRAM_LOG_CHAT_ID'))
    self.client = Client(
      self.app_name,
      session_string=self.string_session
    )
  
  def start(self):
    self.client.start()

  def download_media(self, message_id: int):
    message = self.client.get_messages(self.base_chat_id, message_id)
    file_path = self.client.download_media(message)
    return file_path

  def download_thumbnail(self, message_id: int):
    message = self.client.get_messages(self.base_chat_id, message_id)
    video = message.video

    if video and video.thumbs:
      file_path = self.client.download_media(video.thumbs[0])
      return file_path

  def send_log(self, text: str, photo_file_path: str):
    self.client.send_photo(self.log_chat_id, photo_file_path, text)

  def get_random_message_id(self):
    random_line = random.choice(list(open('./messageIds.txt')))
    return int(random_line)

  def stop(self):
    self.client.stop()

telegram = Telegram()
