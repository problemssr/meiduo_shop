from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from apps.meiduo_admin.views import home, user, images
from apps.meiduo_admin.views.token import MyTokenObtainPairView

urlpatterns = [
    path('authorizations/', MyTokenObtainPairView.as_view()),
    # path('authorizations/', meiduo_token),
    # 日活统计
    path('statistical/day_active/', home.DailyActiveAPIView.as_view()),
    # 日下单用户
    path('statistical/day_orders/', home.DailyOrderCountAPIView.as_view()),

    # user
    path('users/', user.UserAPIView.as_view()),    # 获取图片新增中的 sku展示
    path('skus/simple/', images.ImageSKUAPIView.as_view()),

    #
    # path('skus/categories/', sku.GoodsCategoryAPIView.as_view()),

]
from rest_framework.routers import DefaultRouter

#  1.创建router实例
rouer = DefaultRouter()
# 2. 设置路由
rouer.register('skus/images', images.ImageModelViewSet, basename='images')

################sku#############################
# rouer.register('skus', sku.SKUModelViewSet, basename='skus')

# 3.追加到 urlpatterns
urlpatterns += rouer.urls