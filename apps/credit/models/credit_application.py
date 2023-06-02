from django.db import models

from common.mixins.created import CreatedMixin


class CreditApplication(CreatedMixin):
    name = models.CharField(max_length=100)
