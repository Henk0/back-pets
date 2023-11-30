from django.db import models
from django.contrib.auth.models import AbstractUser

def upload_to(instance, filename):
    return 'images/{filename}'.format(filename=filename)


class User(AbstractUser):
    photo = models.ImageField(
        upload_to=upload_to,
        blank=True,
        null=True)
    phone = models.CharField(max_length=30, blank=True)