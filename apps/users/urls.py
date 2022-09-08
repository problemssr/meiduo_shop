from django.urls import path
from apps.users import views

# 注册转换器
from utils.converters import UsernameConverter
from django.urls import register_converter

register_converter(UsernameConverter, 'username')

urlpatterns = [
    # 判断用户名是否重复
    path('usernames/<username:username>/count/', views.UsernameCountView.as_view())
]
