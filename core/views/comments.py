from rest_framework.viewsets import ModelViewSet

from core.models import Comments 
from core.serializers import CommentsSerializer

class CommentsViewSet(ModelViewSet):
    queryset = Comments.objects.all()
    serializer_class = CommentsSerializer