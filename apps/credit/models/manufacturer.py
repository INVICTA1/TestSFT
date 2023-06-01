from django.db import models

from common.mixins.created import CreatedMixin


class Manufacturer(CreatedMixin):
    name = models.CharField(max_length=100)
