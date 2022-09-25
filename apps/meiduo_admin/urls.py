from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from apps.meiduo_admin.views import home, user, images, sku, permissions
from apps.meiduo_admin.views.token import MyTokenObtainPairView

urlpatterns = [
    path('authorizations/', MyTokenObtainPairView.as_view()),
    # path('authorizations/', meiduo_token),
    # 日活统计
    path('statistical/day_active/', home.DailyActiveAPIView.as_view()),
    # 日下单用户
    path('statistical/day_orders/', home.DailyOrderCountAPIView.as_view()),

    # user
    path('users/', user.UserAPIView.as_view()),  # 获取图片新增中的 sku展示
    path('skus/simple/', images.ImageSKUAPIView.as_view()),

    # 三级分类数据
    path('skus/categories/', sku.GoodsCategoryAPIView.as_view()),
    # sku 中获取 spu的数据
    path('goods/simple/', sku.SPUListAPIView.as_view()),
    #
    # # sku 中获取 spu的规格和规格选项
    path('goods/<int:spu_id>/specs/', sku.SPUSpecAPIView.as_view()),
    #
    # # 权限中 获取 ContentType 的数据
    path('permission/content_types/', permissions.ConentTypeListAPIView.as_view()),
    #
    # # 组中 获取 权限列表数据
    # path('permission/simple/', permissions.GroupPermissionListAPIView.as_view()),
    #
    # # 组中 获取 权限列表数据
    # path('permission/groups/simple/', permissions.SimpleGroupListAPIView.as_view()),
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

################sku#############################
rouer.register('skus', sku.SKUModelViewSet, basename='skus')

###############权限##################################
rouer.register('permission/perms', permissions.PermissionModelViewSet, basename='perms')
#
# ###############组##################################
# rouer.register('permission/groups',permissions.GroupModelViewSet,basename='groups')
#
# ###############普通管理员##################################
# rouer.register('permission/admins',permissions.AdminUserModelViewSet,basename='admins')

# 3.追加到 urlpatterns
urlpatterns += rouer.urls
