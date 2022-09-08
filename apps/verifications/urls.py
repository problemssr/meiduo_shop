from django.urls import path
from apps.verifications import views

from utils.converters import UUIDConverter,PhoneConverter
from django.urls import register_converter

register_converter(UUIDConverter, 'uuid')
register_converter(PhoneConverter, 'phone')

urlpatterns = [
    path('image_codes/<uuid:uuid>/', views.ImageCodeView.as_view()),
    path('sms_codes/<phone:mobile>/', views.SmsCodeView.as_view()),
]
