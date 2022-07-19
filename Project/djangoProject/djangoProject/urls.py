"""djangoProject URL Configuration

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
from django.urls import path, include, re_path
from rest_framework.routers import DefaultRouter

from post import views
from post.views import ImagesPostList

# router = DefaultRouter()
# router.register('images', ImagesPostList, 'images')

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('api/', include(router.urls)),
    path('post/', views.post),
    path('', views.images_post_list),
    path('CBV/', views.CBVPostList.as_view()),
    re_path('CBV/(?P<pk>\d+)', views.CBVPostDetail.as_view()),  # re_path正则
    path('ImagesPost/', views.ImagesPostList.as_view()),
    re_path("ImagesPost/(?P<pk>\d+)", views.ImagesPostDetail.as_view()),
    path("app03/", views.BookInfoGenericAPIView.as_view()),

]
