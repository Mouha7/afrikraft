from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    profile_picture = models.ImageField(upload_to="user/images", blank=True, null=True)
    date_of_birth = models.DateField(null=True, blank=True)
    bio = models.TextField(blank=True, null=True)
    
    def __str__(self) -> str:
        return f"{self.username} : {self.date_of_birth}"