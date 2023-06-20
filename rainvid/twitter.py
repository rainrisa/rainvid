import tweepy
from dotenv import load_dotenv
from os import getenv

load_dotenv()

class Twitter:
  def __init__(self):
    self.consumer_key = getenv('TWITTER_CONSUMER_KEY')
    self.consumer_secret = getenv('TWITTER_CONSUMER_SECRET')
    self.access_token = getenv('TWITTER_ACCESS_TOKEN')
    self.access_token_secret = getenv('TWITTER_ACCESS_TOKEN_SECRET')

    self.client = tweepy.Client(
      consumer_key=self.consumer_key, consumer_secret=self.consumer_secret,
      access_token=self.access_token, access_token_secret=self.access_token_secret
    )
    self.auth = tweepy.OAuth1UserHandler(
      consumer_key=self.consumer_key, consumer_secret=self.consumer_secret,
      access_token=self.access_token, access_token_secret=self.access_token_secret
    )
    self.api = tweepy.API(self.auth)

  def tweet(self, text: str, media_ids: [str] = []):
    return self.client.create_tweet(
      text=text,
      media_ids=media_ids
    )

  def upload_media(self, path: str):
    return self.api.media_upload(path)

twitter = Twitter()