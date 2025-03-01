from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    photo_url = models.URLField(max_length=500, blank=True,null=True)

    def __str__(self):
        return self.username