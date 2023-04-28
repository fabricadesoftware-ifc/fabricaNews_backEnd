from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from core.views import UserProjectFollowViewSet, FeelingViewSet, NewsViewSet

router = DefaultRouter()
router.register(r"feelings", FeelingViewSet)
router.register(r"user_project_follows", UserProjectFollowViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(router.urls)),
]