from django.db import models

from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    roles = models.ManyToManyField('Role')

class Role(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name
