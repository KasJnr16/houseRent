from django.urls import path
from .import views

app_name = "houseInfo"

urlpatterns = [
    path("upload/", views.uploadHome, name="upload"),
    path("<int:pk>", views.viewHomeDetail, name="homeDetail"),
    path("edit/<int:pk>",views.updateHome, name="editHome"),
    path("delete/<int:pk>",views.deleteHome, name="deleteHome"),

]