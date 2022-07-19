from rest_framework import serializers
from post.models import TestPost


class TestPostLogSerializer(serializers.ModelSerializer):
    upload_images = serializers.ImageField()
    text_1 = serializers.CharField(read_only=True)
    text_2 = serializers.CharField(read_only=True)

    class Meta:
        model = TestPost
        fields = ["upload_images", 'text_1', "text_2"]
