from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.http import (
    HttpRequest, 
    HttpResponse,
)


@require_http_methods(["GET"])
def error_404(request: HttpRequest, *args, **kwargs) -> HttpResponse:
    data = {
        "msg": kwargs.get("exception", None)
    }
    return render(request, "error/404.html", data)


@require_http_methods(["GET"])
def error_500(request: HttpRequest, *args, **kwargs) -> HttpResponse:
    data = {
        "msg": kwargs.get("exception", None)
    }
    return render(request, "error/500.html", data)


@require_http_methods(["GET"])
def error_403(request: HttpRequest, *args, **kwargs) -> HttpResponse:
    data = {
        "msg": kwargs.get("exception", None)
    }
    return render(request, "error/403.html", data)


@require_http_methods(["GET"])
def error_400(request: HttpRequest, *args, **kwargs) -> HttpResponse:
    data = {
        "msg": kwargs.get("exception", None)
    }
    return render(request, "error/400.html", data)
