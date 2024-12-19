from django.conf import settings
from django.http import HttpRequest
from django.utils import translation
from django.utils.translation import get_language


def set_locale_from_session_middleware(get_response):
    """Set locale from session, by key settings.SESSION_LANGUAGE_KEY."""
    
    def middleware(request: HttpRequest):
        new_language = request.session.get(settings.SESSION_LANGUAGE_KEY, None)

        if new_language == get_language():
            response = get_response(request)
            return response
        
        translation.activate(new_language)
        response = get_response(request)
        response.set_cookie(settings.LANGUAGE_COOKIE_NAME, new_language)

        return response
    
    return middleware

