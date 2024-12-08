# from django.shortcuts import render
from core.vendors.base.view import BaseTemplateView


class HomeView(BaseTemplateView):
    """Home view."""
    template_name = "reserv/home.html"


# def home(request):
#     return render(request, "reserv/home.html")