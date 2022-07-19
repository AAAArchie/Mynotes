from django.db import models


# 数据模型
class ImagesPost(models.Model):
    # 设置null=True，则仅表示在数据库中该字段可以为空，但使用后台管理添加数据时仍然要需要输入值，因为Django自动做了数据验证不允许字段为空
    # 如果想要在Django中也可以将字段保存为空值，则需要添加另一个参数：blank=True
    # related_name可以支持 user.images_posted 直接获取一个用户的所有照片的queryset
    # 这里允许空值，因为空值可以代表用户未登录
    upload_images = models.ImageField(upload_to='upload_images')  # 应该用单数
    modified_nation = models.CharField(max_length=20, null=True, blank=True)
    time_consuming = models.CharField(max_length=50, null=True, blank=True)
