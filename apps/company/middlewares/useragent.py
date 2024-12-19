from django.http import HttpRequest


def set_useragent_in_request_middleware(get_response):
    """Set useragent in request."""
    
    def middleware(request: HttpRequest):
        setattr(request, "user_agent", request.META["HTTP_USER_AGENT"])
        response = get_response(request)

        return response

    return middleware
