from django.db import models


class Customer(models.Model):
    name = models.CharField(max_length=256)
    address1 = models.CharField(max_length=256, null=True, blank=True)
    address2 = models.CharField(max_length=256, blank=True, null=True)
    city = models.CharField(max_length=128, blank=True, null=True)
    state = models.CharField(max_length=2, blank=True, null=True)
    zip = models.CharField(max_length=12, blank=True, null=True)
    email = models.CharField(max_length=256, blank=True, null=True)

    def __str__(self):
        return self.name

    def invoices(self):
        from invoice.models.inv import Invoice

        return Invoice.objects.filter(customer=self).count()
