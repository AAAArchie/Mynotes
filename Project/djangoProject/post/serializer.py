from rest_framework import serializers
from post.models import ImagesPost


class ImagesPostLogSerializerV2(serializers.ModelSerializer):
    modified_nation = serializers.CharField(read_only=True)
    upload_images = serializers.ImageField()
    time_consuming = serializers.CharField(read_only=True)

    class Meta:
        model = ImagesPost
        fields = ['modified_nation', "upload_images", "time_consuming"]
