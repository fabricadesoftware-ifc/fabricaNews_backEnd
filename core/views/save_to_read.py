from rest_framework.viewsets import ModelViewSet
from core.models import Save_to_read
from core.serializers import Save_to_readSerializer

class Save_to_readViewSet(ModelViewSet):
    queryset = Save_to_read.objects.all()
    serializer_class = Save_to_readSerializer
