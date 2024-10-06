from django.db import models

from apps.common.models import BaseModel


class Loxury(BaseModel):
    name = models.CharField(max_length=225, null=True, blank=True, unique=True)
    image = models.ImageField(
        upload_to='loxury_images/',
        default='images/default-image.jpg',
        null=True, blank=True,
        )
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return f"{self.id}-{self.name}"
