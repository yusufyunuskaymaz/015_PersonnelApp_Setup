from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from datetime import date
from django.contrib.auth.models import User


class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    display_name = models.CharField(max_length=30,blank=True,null=True)
    avatar = models.ImageField(upload_to="pictures", default="avatar.jpg")
    bio = models.TextField(blank=True,null=True)


    def __str__(self):
        return f"{self.user.username}'s Profile"


    

