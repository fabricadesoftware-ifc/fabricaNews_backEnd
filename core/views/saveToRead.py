from rest_framework.viewsets import ModelViewSet
from core.models import SaveToRead
from core.serializers import Save_to_readSerializer


class SaveToReadViewSet(ModelViewSet):
    queryset = SaveToRead.objects.all()  # pylint: disable=E1101
    serializer_class = Save_to_readSerializer
