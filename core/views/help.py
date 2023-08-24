from rest_framework.viewsets import ModelViewSet

from core.models import Help
from core.serializers import HelpSerializer


class HelpViewSet(ModelViewSet):
    queryset = Help.objects.all()  # pylint: disable=E1101
    serializer_class = HelpSerializer
