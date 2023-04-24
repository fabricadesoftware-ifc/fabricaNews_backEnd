from django.contrib import admin
from django.urls import include, path

from rest_framework.routers import DefaultRouter

from core.views import FavoritesViewSet

router = DefaultRouter()
router.register(r"favorites", FavoritesViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(router.urls)),
]