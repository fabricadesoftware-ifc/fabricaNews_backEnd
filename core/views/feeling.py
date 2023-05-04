from rest_framework.viewsets import ModelViewSet
from core.models import Feeling
from core.serializers import FeelingSerializer


class FeelingViewSet(ModelViewSet):
    queryset = Feeling.objects.all()  # pylint: disable=E1101
    serializer_class = FeelingSerializer
