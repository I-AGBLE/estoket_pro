from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("app_users.urls")),
    path("", include("app_main.urls")),
]


if settings.DEBUG:  # only in development
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)