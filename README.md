# BookmarkTweetFastAPI

はてなブックマークとTwitterへの投稿を行うWebAPIです。
Railwayを使うと同一環境を作成できます。


## Usage

同環境を作成した後、Railwayの設定から環境変数を設定してください。
下記の右辺をトークンに置き換える必要があります。

```.dotenv
consumer_key=TwitterのCONSUMER_KEY
consumer_secret=TwitterのCONSUMER_SERCRET
access_token=TwitterのACCECE_TOKEN
access_token_secret=TwitterのACCECE_TOKEN_SECRET
SECURE_TOKEN=ランダムなトークン（認証用の為、なんでも良い）
CONSUMER_KEY=はてなAPIのCONSUMER KEY
CONSUMER_SECRET=はてなAPIのCONSUMER_SECRET
ACCESS_TOKEN=はてなAPIのACCESS_TOKEN
ACCESS_TOKEN_SECRET=はてなAPIのACCESS_TOKEN_SECRET
```

詳しくは [とらメモ](https://96tora.com/) の該当記事を参照してください。



# FastAPI

This example starts up a [FastAPI](https://fastapi.tiangolo.com/) server.

[![Deploy on Railway](https://railway.app/button.svg)](https://railway.app/new/template/-NvLj4?referralCode=milo)
## ✨ Features

- FastAPI
- Python 3

## 💁‍♀️ How to use

- Deploy using the button 👆
- Clone locally and install packages with Pip using `pip install -r requirements.txt` or Poetry using `poetry install`
- Connect to your project using `railway link`
- Run locally using `uvicorn main:app --reload`

## 📝 Notes

- To learn about how to use FastAPI with most of its features, you can visit the [FastAPI Documentation](https://fastapi.tiangolo.com/tutorial/).
- FastAPI provides automatic documentation to call and test your API directly from the browser. You can access it at `/docs` with [Swagger](https://github.com/swagger-api/swagger-ui) or at `/redoc` with [Redoc](https://github.com/Rebilly/ReDoc).
