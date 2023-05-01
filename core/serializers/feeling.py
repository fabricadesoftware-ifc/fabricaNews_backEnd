from rest_framework.serializers import ModelSerializer
from core.models import Feeling


class FeelingSerializer(ModelSerializer):
    class Meta:
        model = Feeling
        fields = "__all__"