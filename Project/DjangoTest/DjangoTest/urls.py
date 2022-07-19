"""DjangoTest URL Configuration

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

from post import views

router = DefaultRouter()

# class RedirectToAPI(RedirectView):
#     url = '/api/'
router.register(r'TestPostViewSet', views.TestPostViewSet, basename="post_post")

urlpatterns = [
    path('admin/', admin.site.urls),

    # FBV 函数视图
    path('FBV_post/', views.FBV_post),
    path('FBV_api_view', views.FBV_api_view),

    # CBV 类视图
    path('CBVAPIViewList/', views.CBVAPIViewList.as_view()),
    re_path('CBVAPIViewDetaill/(?P<pk>\d+)', views.CBVAPIViewDetail.as_view()),  # re_path正则
    path('TestPostMixinList/', views.TestPostMixinList.as_view()),
    re_path("TestPostMixinDetail/(?P<pk>\d+)", views.TestPostMixinDetail.as_view()),
    path("TestPostGenericAPIView/", views.TestPostGenericAPIView.as_view()),
    path("ListCreateAPIView/", views.TestPostGenericAPIView.as_view()),
    path("RetrieveUpdateDestroyAPIView/", views.TestPostGenericAPIView.as_view()),

    # 视图集 路由器
    path('api/', include(router.urls)),
    path(r'api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
