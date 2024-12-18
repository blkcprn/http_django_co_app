from django.contrib import admin
from django.conf import settings
from debug_toolbar.toolbar import debug_toolbar_urls
from django.urls import (
    path, 
    include,
)


urlpatterns = [
    path("admin/", admin.site.urls),
]
if settings.DEBUG and not settings.TESTING:
    urlpatterns += [
        *debug_toolbar_urls()
    ]
