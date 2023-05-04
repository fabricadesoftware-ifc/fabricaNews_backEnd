from rest_framework.serializers import ModelSerializer

from core.models import NewsFeel

class NewsFeelSerializer(ModelSerializer):
    class Meta:
        model = NewsFeel
        fields = '__all__'