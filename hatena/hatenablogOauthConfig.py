############### Oauth認証URL(共通） ###############

# Temporary Credential Request URL
request_url = 'https://www.hatena.com/oauth/initiate?scope=read_public,write_public'

# Resource Owner Authorization URL
authorize_url_PC = 'https://www.hatena.ne.jp/oauth/authorize' #pc
authorize_url_SmartPhone = 'https://www.hatena.ne.jp/touch/oauth/authorize' # スマホ
authorize_url_Mobile = 'https://www.hatena.ne.jp/mobile/oauth/authorize' # 携帯電話

# Token Request URL
access_token_url = 'https://www.hatena.com/oauth/token'

# Callback URI
callback_uri = 'oob'