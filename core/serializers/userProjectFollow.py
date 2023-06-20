from rest_framework.serializers import ModelSerializer
from user.models import UserProjectFollow

class UserProjectFollowSerializer(ModelSerializer):
    class Meta:
        model = UserProjectFollow
        fields = "__all__"