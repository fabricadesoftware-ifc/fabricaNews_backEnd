from rest_framework.serializers import ModelSerializer
from core.models import UserProjectFollow

class UserProjectFollowSerializer(ModelSerializer):
    class Meta:
        model = UserProjectFollow
        fields = "__all__"