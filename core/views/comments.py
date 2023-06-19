from rest_framework.viewsets import ModelViewSet

from core.models import Comments
from core.serializers import CommentsSerializer


class CommentsViewSet(ModelViewSet):
    queryset = Comments.objects.all()  # pylint: disable=E1101
    serializer_class = CommentsSerializer
