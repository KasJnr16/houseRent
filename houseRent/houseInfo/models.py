from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)

    # making the name plural
    # basically config for model
    class Meta:
        ordering = ("name",)
        verbose_name_plural = "Categories"

    def __str__(self) -> str:
        return self.name

class House(models.Model):
    category = models.ForeignKey(Category, related_name="items", on_delete=models.CASCADE)
    house_name = models.CharField(max_length=10)
    description = models.TextField(blank=True, null=True)
    location = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=6 ,decimal_places=2)
    image = models.ImageField(upload_to="house_images") #install Pillow to handle pics
    image1 = models.ImageField(upload_to="house_images" ,null=True) #install Pillow to handle pics
    image2 = models.ImageField(upload_to="house_images" ,null=True) #install Pillow to handle pics
    for_rent = models.BooleanField(default=True)
    created_by = models.ForeignKey(User, related_name="houses", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.house_name


