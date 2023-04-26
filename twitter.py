# tweetを投稿
# -------------------------------------------------------------------------

import tweepy
import os

# -------------------------------------------------------------------------

# Twitter情報。
# ＊＊＊＊＊＊＊＊には自分自身のAPIキーなどを入力してください
consumer_key = os.environ.get("consumer_key")
consumer_secret = os.environ.get("consumer_secret")
access_token = os.environ.get("access_token")
access_token_secret = os.environ.get("access_token_secret")


# -------------------------------------------------------------------------
# Twitterの認証
def aurhor():
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)

    # 　”wait_on_rate_limit = True”　利用制限にひっかかた時に必要時間待機する
    api = tweepy.API(auth, wait_on_rate_limit=True)
    return api


# -------------------------------------------------------------------------
# ツイートを投稿
def tweet(api, tweet_text: str):
    print(tweet_text)
    api.update_status(tweet_text)
