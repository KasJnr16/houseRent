from django.urls import path
from .import views

app_name = "userProfile"

urlpatterns = [
    path("",views.userProfile, name="profile"),
]