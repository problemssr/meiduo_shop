# 当系统的功能 不能满足我们需求的时候就要重写

from rest_framework_simplejwt.tokens import RefreshToken


def get_tokens_for_user(user):
    # token,        认证成功之后,生成的token
    # user=None,    认证成功之后的用户
    # request=None  请求
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
        'username': user.username,
        'id': user.id
    }
