from django.db import models


# 数据模型
from users.models import UserProfile


class TestPost(models.Model):
    upload_images = models.ImageField(upload_to='upload_images')  # 应该用单数
    text_1 = models.CharField(max_length=20, null=True, blank=True)
    text_2 = models.CharField(max_length=50, null=True, blank=True)
    """参考：https://docs.djangoproject.com/zh-hans/4.0/ref/models/fields/#field-attribute-reference"""
    user = models.ForeignKey(to=UserProfile, on_delete=models.CASCADE, related_name='test_foreignkey',
                             null=True, blank=True, default=None)


class CdsNasClusterInfo(models.Model):
    """
    NasClusterInfo
    database:
    """
    availability_area = models.CharField(max_length=255, blank=True, null=True, verbose_name="可用区")
    cluster_name = models.CharField(max_length=255, blank=True, null=True, verbose_name="集群名称")
    total_size = models.CharField(max_length=255, blank=True, null=True, verbose_name="集群存储总容量")
    used_size = models.CharField(max_length=255, blank=True, null=True, verbose_name=" 集群存储已用容量")
    capacity_usage = models.CharField(max_length=255, blank=True, null=True, verbose_name="存储使用率")
    sold_size = models.CharField(max_length=255, blank=True, null=True, verbose_name="集群已分配容量")
    sold_usage = models.CharField(max_length=255, blank=True, null=True, verbose_name="集群已分配比率")
    cluster_status = models.CharField(max_length=255, blank=True, null=True, verbose_name="集群状态")

    class Meta:
        db_table = ''
        verbose_name = ''
