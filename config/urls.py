from django.contrib import admin
from django.urls import include, path

from rest_framework.routers import DefaultRouter

from core.views import Save_to_readViewSet

router = DefaultRouter()
router.register(r"save_to_read", Save_to_readViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(router.urls)),
]