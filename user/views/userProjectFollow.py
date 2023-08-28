from rest_framework.viewsets import ModelViewSet

from user.models import UserProjectFollow
from user.serializers.userProjectFollow import UserProjectFollowSerializer


class UserProjectFollowViewSet(ModelViewSet):
    queryset = UserProjectFollow.objects.all()  # pylint: disable=E1101
    serializer_class = UserProjectFollowSerializer
