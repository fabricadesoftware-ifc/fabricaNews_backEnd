from rest_framework.serializers import ModelSerializer

from core.models import Comments


class CommentsSerializer(ModelSerializer):
    class Meta:
        model = Comments
        fields = "__all__"
