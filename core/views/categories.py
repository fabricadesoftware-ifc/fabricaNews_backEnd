from rest_framework.viewsets import ModelViewSet
from core.models import Category
from core.serializers import CategorySerializer


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()  # pylint: disable=E1101
    serializer_class = CategorySerializer
