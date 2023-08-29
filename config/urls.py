from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from uploader.router import router as uploader_router
from .routers import router

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(router.urls)),
    path("api/media/", include(uploader_router.urls)),
]

urlpatterns += static(settings.MEDIA_ENDPOINT, document_root=settings.MEDIA_ROOT)
