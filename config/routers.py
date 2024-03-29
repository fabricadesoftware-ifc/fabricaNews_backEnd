from rest_framework.routers import DefaultRouter

from core.views import (
    CategoryViewSet,
    CommentsViewSet,
    FavoritesViewSet,
    FeelingViewSet,
    HelpViewSet,
    NewsFeelViewSet,
    NewsViewSet,
    ReactionViewSet,
    SaveToReadViewSet,
)
from user.views import UserProjectFollowViewSet

router = DefaultRouter()
router.register(r"newsfeel", NewsFeelViewSet)
router.register(r"categories", CategoryViewSet)
router.register(r"favorites", FavoritesViewSet)
router.register(r"feelings", FeelingViewSet)
router.register(r"news", NewsViewSet)
router.register(r"userProjectFollows", UserProjectFollowViewSet)
router.register(r"savetoread", SaveToReadViewSet)
router.register(r"reactions", ReactionViewSet)
router.register(r"comments", CommentsViewSet)
router.register(r"helps", HelpViewSet)
