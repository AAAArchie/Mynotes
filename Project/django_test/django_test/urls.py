"""django_test URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include
from rest_framework.routers import DefaultRouter

from post_app import views
from post_app import viewsets

router = DefaultRouter()

# class RedirectToAPI(RedirectView):
#     url = '/api/'
# 视图集 url
router.register(r'TestPostViewSet', viewsets.TestPostViewSet, basename="post_post")
router.register(r'TestPostViewSetV1', viewsets.TestPostViewSetV1, basename="post_post_v1")
router.register(r'TestPostViewSetV2', viewsets.TestPostViewSetV2, basename="post_post_v2")

urlpatterns = [
    path('admin/', admin.site.urls),

    # FBV 函数视图
    path('FBV_post/', views.FBV_post),
    path('FBV_api_view', views.FBV_api_view),

    # CBV 类视图
    path('CBVAPIViewList/', viewsets.CBVAPIViewList.as_view()),
    re_path('CBVAPIViewDetaill/(?P<pk>\d+)', viewsets.CBVAPIViewDetail.as_view()),  # re_path正则
    path('TestPostMixinList/', viewsets.TestPostMixinList.as_view()),
    re_path("TestPostMixinDetail/(?P<pk>\d+)", viewsets.TestPostMixinDetail.as_view()),
    path("TestPostGenericAPIView/", viewsets.TestPostGenericAPIView.as_view()),
    path("ListCreateAPIView/", viewsets.TestPostGenericAPIView.as_view()),
    path("RetrieveUpdateDestroyAPIView/", viewsets.TestPostGenericAPIView.as_view()),

    # 视图集 路由器
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
