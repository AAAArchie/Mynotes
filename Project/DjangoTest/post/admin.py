from django.contrib import admin

from .models import TestPost

# 注册TestPost到admin中
admin.site.register(TestPost)
