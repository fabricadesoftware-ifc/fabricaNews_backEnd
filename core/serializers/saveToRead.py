from rest_framework.serializers import ModelSerializer
from core.models import saveToRead

class SaveToReadSerializer(ModelSerializer):
    class Meta:
        model = saveToRead
        fields = "__all__"