from .views import HomeView
from django.urls import path


app_name = "company"


urlpatterns = [
	path("home/", HomeView.as_view(), name="home"),
]