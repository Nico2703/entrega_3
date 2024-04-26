from django.urls import path
from . import views

app_name = "compra"

urlpatterns = [
    path("home/", views.home, name="home"),
]