from django.db import models

from django.contrib.auth.models import AbstractUser
from ckeditor.fields import RichTextField

from apps.common.models import BaseModel


class User(BaseModel, AbstractUser):
    GENDER = (
        ('male', ('Male')),
        ('female', ('Female')),
    )

    description = RichTextField(null=True, blank=True)
    image = models.ImageField(upload_to='avatars/', null=True, blank=True, default='images/default-image.jpg')
    phone_number = models.CharField(max_length=225, null=True, blank=True)
    gender = models.CharField(choices=GENDER, max_length=225, null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True)

    def __str__(self):
        if self.get_full_name():
            return f"{self.id}-{self.get_full_name()}"
        
        elif self.email:
            return f"{self.id}-{self.email}"
        
        else:
            return f"{self.id}-{self.username}"
