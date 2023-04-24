from django.contrib import admin
from django.urls import include, path

from rest_framework.routers import DefaultRouter

from core.views import CategoryViewSet

router = DefaultRouter()
router.register('categories', CategoryViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include(router.urls)),
]
