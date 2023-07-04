from telegram import telegram
from twitter import twitter
from dotenv import load_dotenv
from os import getenv

load_dotenv()

telegram.start()

me = twitter.get_me()
random_message_id = telegram.get_random_message_id()
file_path = telegram.download_thumbnail(random_message_id)
media_upload = twitter.upload_media(file_path)
caption = getenv('TWITTER_DEFAULT_CAPTION')
tweet = twitter.tweet(
  caption,
  media_ids=[media_upload.media_id_string]
)
tweet_url = f"https://twitter.com/{me['username']}/status/{tweet.data['id']}"
telegram.send_log(tweet_url)

telegram.stop()