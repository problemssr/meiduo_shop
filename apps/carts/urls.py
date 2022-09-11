from django.urls import path

from apps.carts import views

urlpatterns = [
    # 购物车增删改查
    path('carts/', views.CartsView.as_view()),
    # 全选购物车
    path('carts/selection/', views.CartsSelectAllView.as_view()),
    # 简单购物车
    path('carts/simple/', views.CartsSimpleView.as_view()),

]
