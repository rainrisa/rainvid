# Rainvid

Auto post daily Telegram media into Twitter

## Usage

- Set up a group containing media
- Get all media message ids from that group and store it on messageIds.txt
- Fill up .env requirements
- Generate string session with `python rainvid/get_string_session.py`
- Add .env file to GitHub secret https://stackoverflow.com/a/63350136
