from rest_framework.viewsets import ModelViewSet
from core.models import Favorites
from core.serializers import FavoritesSerializer

class FavoritesViewSet(ModelViewSet):
    queryset = Favorites.objects.all()
    serializer_class = FavoritesSerializer