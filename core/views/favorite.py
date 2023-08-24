from rest_framework.viewsets import ModelViewSet

from core.models import Favorites
from core.serializers import FavoritesSerializer


class FavoritesViewSet(ModelViewSet):
    queryset = Favorites.objects.all()  # pylint: disable=E1101
    serializer_class = FavoritesSerializer
