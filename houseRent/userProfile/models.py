from django.db import models
from django.contrib.auth.models import User

class ProfileInformation(models.Model):
     user = models.ForeignKey(User, related_name="profile", on_delete=models.CASCADE)
     first_name = models.CharField(max_length=20)
     last_name = models.CharField(max_length=20)
     image = models.ImageField(upload_to="profile_picture")

     def __str__(self) -> str:
          return f"{self.first_name} {self.last_name}"