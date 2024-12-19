from django.conf import settings
from django.contrib import messages
from core.vendors import messages as msg
from core.vendors.helpers.shortcuts import redirect_back
from django.views.decorators.http import require_http_methods
from django.http import (
    HttpRequest, 
    HttpResponse,
)


@require_http_methods(["GET"])
def chenge_language(request: HttpRequest, lang_code: str = settings.LANGUAGE_CODE) -> HttpResponse:
    """Set session language key, and redirect back."""
    language_codes = settings.AVAILABLE_LANGUAGE_CODES  # or get from Company.settings.languages
    if lang_code in language_codes:
        request.session[settings.SESSION_LANGUAGE_KEY] = lang_code
    else:
        messages.add_message(request, messages.INFO, msg.UNAVAILABLE_LANGUAGE)
    return redirect_back(request)


@require_http_methods(["GET"])
def chenge_currency(request: HttpRequest, currency_code: str = settings.CURRENCY_CODE) -> HttpResponse:
    """Set session currency key, and redirect back."""
    currency_codes = settings.AVAILABLE_CURRENCY_CODES  # or get from Company.settings.currencies
    if currency_code in currency_codes:
        request.session[settings.SESSION_CURRENCY_KEY] = currency_code
    else:
        messages.add_message(request, messages.INFO, msg.UNAVAILABLE_CURRENCY)
    return redirect_back(request)