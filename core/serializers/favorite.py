from rest_framework.serializers import ModelSerializer
from core.models import Favorites


class FavoritesSerializer(ModelSerializer):
    class Meta:
        model = Favorites
        fields = "__all__"
