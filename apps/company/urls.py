from django.urls import path
from .views import company


app_name = "company"


urlpatterns = [
	path("home/", company.home, name="home"),
]