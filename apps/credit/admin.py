from django.contrib import admin

from credit.models import CreditApplication, Product, Contract, Manufacturer

# admin.site.register(CreditApplication, Product, Contract, Manufacturer)
admin.site.register(CreditApplication)
admin.site.register(Product)
admin.site.register(Contract)
admin.site.register(Manufacturer)


