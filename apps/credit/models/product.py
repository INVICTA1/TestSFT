from django.db import models

from common.mixins.created import CreatedMixin
from credit.models import Manufacturer


class Product(CreatedMixin):
    name = models.CharField(max_length=100)
    manufacturer = models.ForeignKey(
        Manufacturer, on_delete=models.CASCADE, related_name='products'
    )


