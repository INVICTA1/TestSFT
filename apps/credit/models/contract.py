from django.db import models

from common.mixins.created import CreatedMixin
from credit.models import CreditApplication


class Contract(CreatedMixin):
    credit_application = models.ForeignKey(
        CreditApplication, on_delete=models.CASCADE, related_name='contracts'
    )
