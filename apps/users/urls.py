from django.urls import path
from apps.users import views

# 注册转换器
from utils.converters import UsernameConverter, PhoneConverter
from django.urls import register_converter

register_converter(UsernameConverter, 'username')
register_converter(PhoneConverter, 'phone')

urlpatterns = [
    # 判断用户名是否重复
    path('usernames/<username:username>/count/', views.UsernameCountView.as_view()),
    # 判断手机号是否重复
    path('mobiles/<phone:phone>/count/', views.PhoneCountView.as_view()),
    # 注册
    path('register/', views.RegisterView.as_view()),
    # 登录
    path('login/', views.LoginView.as_view()),
    # 退出
    path('logout/', views.LogoutView.as_view()),
    # 退出
    path('info/', views.CenterView.as_view()),

]
