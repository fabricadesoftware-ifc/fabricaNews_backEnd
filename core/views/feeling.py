from rest_framework.viewsets import ModelViewSet
from core.models import Feeling
from core.serializers import FeelingSerializer


class FeelingViewSet(ModelViewSet):
    queryset = Feeling.objects.all()
    serializer_class = FeelingSerializer