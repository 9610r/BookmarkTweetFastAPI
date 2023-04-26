import requests
from requests_oauthlib import OAuth1
import os

API_KEY = os.environ.get("CONSUMER_KEY")
SECRET_KEY = os.environ.get("CONSUMER_SECRET")
ACCESS_TOKEN = os.environ.get("ACCESS_TOKEN")
ACCESS_TOKEN_SECRET = os.environ.get("ACCESS_TOKEN_SECRET")


auth = OAuth1(
  API_KEY,
  SECRET_KEY,
  ACCESS_TOKEN,
  ACCESS_TOKEN_SECRET
)

def bookmark(bookmark_url: str):
  bookmark_api_url = "https://bookmark.hatenaapis.com/rest/1/my/bookmark"
  print(requests.post(bookmark_api_url + "?url=" + bookmark_url, auth=auth).content)
