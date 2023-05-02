from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
import os


# Create your models here.

class User(AbstractUser):
    followings = models.ManyToManyField('self', symmetrical=False, related_name='followers')
    profile_img = models.ImageField(upload_to='profile/', blank=True)

