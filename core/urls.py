from django.contrib import admin
from django.conf import settings
from debug_toolbar.toolbar import debug_toolbar_urls
from django.urls import (
    path, 
    include,
)
from django.conf.urls import (
	handler400,
	handler404, 
	handler500, 
	handler403, 
)


urlpatterns = [
    path("admin/", admin.site.urls),

    path("", include("apps.company.urls", namespace="company")),

    path("i18n/", include("django.conf.urls.i18n")),
]
if settings.DEBUG and not settings.TESTING:
    urlpatterns += [
        *debug_toolbar_urls()
    ]


handler400 = "apps.error.views.error_400"
handler403 = "apps.error.views.error_403"
handler404 = "apps.error.views.error_404"
handler500 = "apps.error.views.error_500"