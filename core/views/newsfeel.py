
from rest_framework.viewsets import ModelViewSet

from core.models import NewsFeel
from core.serializers import NewsFeelSerializer

class NewsFeelViewSet(ModelViewSet):
    queryset = NewsFeel.objects.all()
    serializer_class = NewsFeelSerializer

