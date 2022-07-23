from rest_framework import serializers
from post_app.models import TestPost, CdsNasClusterInfo


class TestPostLogSerializer(serializers.ModelSerializer):
    upload_images = serializers.ImageField()
    text_1 = serializers.CharField(read_only=True)
    text_2 = serializers.CharField(read_only=True)

    class Meta:
        model = TestPost
        fields = ["upload_images", 'text_1', "text_2"]


class CdsNasClusterInfoSerializer(serializers.ModelSerializer):
    """
    NasClusterInfo序列化
    """

    class Meta:
        model = CdsNasClusterInfo
        fields = '__all__'
