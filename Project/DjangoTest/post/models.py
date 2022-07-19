from django.db import models


# 数据模型
class TestPost(models.Model):
    upload_images = models.ImageField(upload_to='upload_images')  # 应该用单数
    text_1 = models.CharField(max_length=20, null=True, blank=True)
    text_2 = models.CharField(max_length=50, null=True, blank=True)
