from rest_framework.viewsets import ModelViewSet

from core.models import Reaction
from core.serializers import ReactionSerializer


class ReactionViewSet(ModelViewSet):
    queryset = Reaction.objects.all()  # pylint: disable=E1101
    serializer_class = ReactionSerializer
