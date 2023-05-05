from rest_framework.serializers import ModelSerializer

from core.models import Reaction


class ReactionSerializer(ModelSerializer):
    class Meta:
        model = Reaction
        fields = "__all__"
