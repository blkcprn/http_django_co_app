from django.urls import path
from .views import (
    HomeView,
    chenge_language,
    chenge_currency,
)


app_name = "company"


urlpatterns = [
    path("home/", HomeView.as_view(), name="home"),

    path("change-language/{str:lang_code}/", chenge_language, name="chenge_language"),
    path("change-currency/{str:currency_code}/", chenge_currency, name="chenge_currency"),
]