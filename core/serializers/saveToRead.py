from rest_framework.serializers import ModelSerializer
from core.models import SaveToRead

class SaveToReadSerializer(ModelSerializer):
    class Meta:
        model = SaveToRead
        fields = "__all__"