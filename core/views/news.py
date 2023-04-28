from rest_framework import ModelViewsSet
from core.models import News
from core.serializers import NewsSerializer

class NewsViewSet(ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer