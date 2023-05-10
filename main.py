from fastapi import FastAPI
from pydantic import BaseModel
import os

app = FastAPI()
SECURE_TOKEN = os.environ.get("SECURE_TOKEN")

class Msg(BaseModel):
    msg: str

class Tweet(BaseModel):
    token: str
    title: str
    url: str
    text: str

    class Config:
        orm_mode = True

@app.get("/")
async def root():
    return

# POSTエンドポイント
@app.post("/post")
async def create_tweet(item: Tweet):
    # トークンがあっているかを確認
    if item.token != SECURE_TOKEN:
        # トークンが間違っていた場合は例外を投げる
        return {"error": f"This token is invailed."}

    from hatena import post
    from twitter import twitter
    post_text = ""

    if url.startswith("chrome://"):
        # `url`が`chrome://`で始まる場合はChromeの内部リンクなので、ブックマークしない。
        # ツイート機能だけはAPIの利用制限が確認できるように残しておく。
        post_text = f"{item.text}"
    else:
        post.bookmark(item.url)
        post_text = f"{item.title}\n{item.url}\n{item.text}"

    api = twitter.aurhor()
    twitter.tweet(api, post_text)
    print("Tweet complete")

    return item.text
