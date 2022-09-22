from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('authorizations/', TokenObtainPairView.as_view()),
    # path('authorizations/', meiduo_token),
]
