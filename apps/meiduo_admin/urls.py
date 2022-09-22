from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from apps.meiduo_admin.views import MyTokenObtainPairView

urlpatterns = [
    path('authorizations/', MyTokenObtainPairView.as_view()),
    # path('authorizations/', meiduo_token),
]
