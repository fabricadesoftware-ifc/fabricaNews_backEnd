from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from core.views import CategoryViewSet, FeelingViewSet, NewsFeelViewSet

router = DefaultRouter()
router.register(r"newsfeel", NewsFeelViewSet)
router.register(r"categories", CategoryViewSet)
router.register(r"feelings", FeelingViewSet)

urlpatterns = [path("admin/", admin.site.urls), path("", include(router.urls))]
