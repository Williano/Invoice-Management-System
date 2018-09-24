from django.db import models


class Customer(models.Model):
    name = models.CharField(max_length=256)
    address1 = models.CharField(max_length=256, blank=True)
    address2 = models.CharField(max_length=256, blank=True)
    city = models.CharField(max_length=128, blank=True)
    state = models.CharField(max_length=2, blank=True)
    zip = models.CharField(max_length=12, blank=True)
    email = models.CharField(max_length=256, blank=True)

    def __str__(self):
        return self.name

    def invoices(self):
        from invoice.models.inv import Invoice

        return Invoice.objects.filter(customer=self).count()
