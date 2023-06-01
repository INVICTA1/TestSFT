from django.db import models

from common.mixins.created import CreatedMixin
from credit.models import Product


class CreditApplication(CreatedMixin):
    name = models.CharField(max_length=100)
    products = models.ManyToManyField(Product, through='ProductInCreditApplication')


class ProductInCreditApplication(CreatedMixin):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    credit_application = models.ForeignKey(
        CreditApplication, on_delete=models.CASCADE
    )
