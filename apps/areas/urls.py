from django.urls import path
from apps.areas import views

urlpatterns = [
    # 省
    path('areas/', views.AreaView.as_view()),
    # 市县
    path('areas/<id>/', views.SubAreaView.as_view()),
]
