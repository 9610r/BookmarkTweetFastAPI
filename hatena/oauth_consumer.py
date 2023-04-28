# Windows用

import urllib
import webbrowser
import requests
from requests_oauthlib import OAuth1
import hatenablogOauthConfig


########## 設定用ファイル参照 ##########

API_KEY = hatenablogOauthConfig.CONSUMER_KEY

SECRET_KEY = hatenablogOauthConfig.CONSUMER_SECRET

request_url = hatenablogOauthConfig.request_url

authorize_url = hatenablogOauthConfig.authorize_url_PC # PC用URL

access_token_url = hatenablogOauthConfig.access_token_url

callback_uri = hatenablogOauthConfig.callback_uri



########## access token取得関数 ##########

def oauth_requests():
    # request token 取得
    auth = OAuth1(API_KEY, SECRET_KEY, callback_uri=callback_uri)
    r = requests.post(request_url, auth=auth)
    request_token = dict(urllib.parse.parse_qsl(r.text))


    # ユーザー認証
    # ブラウザが開き、ユーザ許可を行う
    webbrowser.open('%s?oauth_token=%s&perms=delete' % (authorize_url, request_token['oauth_token']))


    # 外部アプリ連携のユーザ許可後にコマンドラインに表示される。PINコードを入力する
    oauth_verifier = input("Please input PIN code:")
    auth = OAuth1(
        API_KEY,
        SECRET_KEY,
        request_token['oauth_token'],
        request_token['oauth_token_secret'],
        verifier=oauth_verifier)
    r = requests.post(access_token_url, auth=auth)

    access_token = dict(urllib.parse.parse_qsl(r.text))
    return access_token

if __name__ == '__main__':
    # アクセストークンを取得して、表示する
    print(oauth_requests())