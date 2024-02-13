from django.urls import path
from .import views

app_name = "core"

urlpatterns = [
    path("signup/", views.signUp, name="signUp"),
    path("", views.welcome, name="welcome"),
    path("home/", views.index, name="home"),
    path("map/", views.map, name="map"),

]