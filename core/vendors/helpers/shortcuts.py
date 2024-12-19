from django.conf import settings
from django.shortcuts import redirect
from django.http import (
    HttpRequest, 
    HttpResponse,
)


def redirect_back(request: HttpRequest, or_to_url: str = settings.HOME_URL) -> HttpResponse:
    """Redirect back or to or_to_url (optional, default settings.HOME_URL)."""
    return redirect(request.META.get("HTTP_REFERER", or_to_url))