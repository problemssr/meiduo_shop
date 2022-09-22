from django.shortcuts import render

# Create your views here.
from rest_framework_simplejwt.views import TokenObtainPairView

from apps.meiduo_admin.serializers import MyTokenObtainPairSerializer


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
