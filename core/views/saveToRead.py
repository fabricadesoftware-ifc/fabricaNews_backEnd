from rest_framework.viewsets import ModelViewSet

from core.models import SaveToRead
from core.serializers import SaveToReadSerializer


class SaveToReadViewSet(ModelViewSet):
    queryset = SaveToRead.objects.all()  # pylint: disable=E1101
    serializer_class = SaveToReadSerializer
