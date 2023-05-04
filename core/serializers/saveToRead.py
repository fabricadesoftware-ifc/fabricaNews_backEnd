from rest_framework.serializers import ModelSerializer
from core.models import saveToRead

class Save_to_readSerializer(ModelSerializer):
    class Meta:
        model = saveToRead
        fields = "__all__"