from django.urls import path
from apps.users import views
urlpatterns=[
    # 判断用户名是否重复
    path('usernames/<username>/count/',views.UsernameCountView.as_view())
]