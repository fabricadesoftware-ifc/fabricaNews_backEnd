from rest_framework.serializers import ModelSerializer

from core.models import News


class NewsSerializer(ModelSerializer):
    class Meta:
        model = News
        fields = "__all__"
