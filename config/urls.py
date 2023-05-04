from django.contrib import admin
from django.urls import include, path

from rest_framework.routers import DefaultRouter

from core.views import (
    CategoryViewSet,
    FavoritesViewSet,
    FeelingViewSet,
    NewsViewSet,
    NewsFeelViewSet,
    SaveToReadViewSet,
    CommentsViewSet,
    UserProjectFollowViewSet,
)

router = DefaultRouter()
router.register(r"newsfeel", NewsFeelViewSet)
router.register(r"categories", CategoryViewSet)
router.register(r"favorites", FavoritesViewSet)
router.register(r"feelings", FeelingViewSet)
router.register(r"userProjectFollows", UserProjectFollowViewSet)
router.register(r"savetoread", SaveToReadViewSet)
router.register(r"comments", CommentsViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(router.urls)),
]
