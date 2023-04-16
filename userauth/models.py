from django.db import models

# users/models.py

from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):

    email = models.EmailField(blank=False, max_length=254, verbose_name="email address")
    first_name=models.TextField(max_length=256, blank=True)
    last_name=models.TextField(max_length=256, blank=True)

    USERNAME_FIELD = "username"   
    EMAIL_FIELD = "email"       