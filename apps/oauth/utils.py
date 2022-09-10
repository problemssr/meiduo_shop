from mieShop import settings
# 1. 导入 itsdangerous的类
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer


def generic_openid(openid):
    s = Serializer(secret_key=settings.SECRET_KEY, expires_in=3600)
    access_token = s.dumps({'openid': openid})

    return access_token.decode()


def check_access_token(access_token):
    s = Serializer(secret_key=settings.SECRET_KEY, expires_in=3600)
    try:
        res = s.loads(access_token)
    except Exception:
        return None
    else:
        return res.get('openid')
