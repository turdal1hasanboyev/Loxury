from django.db import models

from ckeditor.fields import RichTextField

from apps.common.models import BaseModel


class Contact(BaseModel):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    message = RichTextField(null=True, blank=True)

    def __str__(self):
        return f"{self.id}-{self.name}"
