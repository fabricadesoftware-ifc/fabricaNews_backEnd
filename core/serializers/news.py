from rest_framework.serializers import ModelSerializer, SlugRelatedField
from core.models import News
from uploader.models import Image
from uploader.serializers import ImageSerializer


class NewsSerializer(ModelSerializer):
    imageNew_attachment_key = SlugRelatedField(
        source="imageNew",
        queryset=Image.objects.all(),
        slug_field="attachment_key",
        required=False,
        write_only=True,
    )
    imageNew = ImageSerializer(required=False, read_only=True)


class NewsDetailSerializer(ModelSerializer):
    imageNew = ImageSerializer(required=False)
