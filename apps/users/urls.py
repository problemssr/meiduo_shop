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
    # 邮件
    path('emails/', views.EmailView.as_view()),
    # 验证邮件
    path('emails/verification/', views.EmailVerifyView.as_view()),
    # 新增住址
    path('addresses/create/', views.AddressCreateView.as_view()),
    # 查询住址
    path('addresses/', views.AddressView.as_view()),
    # 修改|删除地址
    path('addresses/<address_id>/', views.UpdateDestroyAddressView.as_view()),
    # 默认地址
    path('addresses/<address_id>/default/', views.DefaultAddressView.as_view()),
    # 修改地址标题
    path('addresses/<address_id>/title/', views.DefaultAddressView.as_view()),
    # 修改密码
    path('password/', views.ChangePasswordView.as_view()),
    # 查询|添加历史记录
    path('browse_histories/', views.UserHistoryView.as_view())

]
