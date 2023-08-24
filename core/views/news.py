from rest_framework.viewsets import ModelViewSet

from core.models import News
from core.serializers import NewsSerializer


class NewsViewSet(ModelViewSet):
    queryset = News.objects.all()  # pylint: disable=E1101
    serializer_class = NewsSerializer
