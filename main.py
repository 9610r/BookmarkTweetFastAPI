from fastapi import FastAPI
from pydantic import BaseModel
from urllib.error import HTTPError
import os

app = FastAPI()
SECURE_TOKEN = os.environ.get("SECURE_TOKEN")

class Msg(BaseModel):
    msg: str

class Tweet(BaseModel):
    token: str
    text: str

@app.get("/")
async def root():
    return {"message": "Hello World. Welcome to FastAPI!"}


@app.get("/path")
async def demo_get():
    return {"message": "This is /path endpoint, use a post request to transform the text to uppercase"}


@app.post("/path")
async def demo_post(inp: Msg):
    return {"message": inp.msg.upper()}


@app.get("/path/{path_id}")
async def demo_get_path_id(path_id: int):
    return {"message": f"This is /path/{path_id} endpoint, use post request to retrieve result"}

# POSTエンドポイント
@app.post("/post")
async def create_tweet(item: Tweet):
    # トークンがあっているかを確認
    if item.token != SECURE_TOKEN:
        # トークンが間違っていた場合は例外を投げる
        return {"error": f"This token is invailed."}

    # トークンがあっていた場合は、処理を実行
    import twitter
    api = twitter.aurhor()
    twitter.tweet(api, item.text)
    print("Tweet complete")
    return item.text
