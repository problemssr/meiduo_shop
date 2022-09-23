from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from apps.meiduo_admin.views import home, user
from apps.meiduo_admin.views.token import MyTokenObtainPairView

urlpatterns = [
    path('authorizations/', MyTokenObtainPairView.as_view()),
    # path('authorizations/', meiduo_token),
    # 日活统计
    path('statistical/day_active/', home.DailyActiveAPIView.as_view()),
    # 日下单用户
    path('statistical/day_orders/', home.DailyOrderCountAPIView.as_view()),

    # user
    path('users/', user.UserAPIView.as_view()),
]
