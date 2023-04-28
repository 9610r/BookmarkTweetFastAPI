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
    post.bookmark(item.url)

    # トークンがあっていた場合は、処理を実行
    import twitter
    api = twitter.aurhor()

    post_text = item.title + "\n" + item.url + "\n" + item.text
    twitter.tweet(api, post_text)
    print("Tweet complete")
    return item.text
