from django.db import models

from django.contrib.auth.models import AbstractUser

from apps.common.models import BaseModel


class User(BaseModel, AbstractUser):
    phone = models.CharField(max_length=25, null=True, blank=True)
