from django.contrib import admin
from django.urls import include, path

from rest_framework import DefaultRouter
from core.views import NewsViewSet

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include(router.urls)),
]