from rest_framework.viewsets import ModelViewSet
from core.models import UserProjectFollow
from core.serializers import UserProjectFollowSerializer


class UserProjectFollowViewSet(ModelViewSet):
    queryset = UserProjectFollow.objects.all()  # pylint: disable=E1101
    serializer_class = UserProjectFollowSerializer
