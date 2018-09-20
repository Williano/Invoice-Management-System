from __future__ import unicode_literals

import uuid
from django.db import models

# Create your models here.


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
        return Invoice.objects.filter(customer=self).count()


class Invoice(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    invoice_code = models.UUIDField(default=uuid.uuid4, editable=False)
    valid = models.BooleanField(default=True)
    date_created = models.DateField(auto_now_add=True)
    expiration_date = models.DateField(null=False, blank=False)
    status = models.CharField(max_length=10)

    def __str__(self):
        return str(self.id)

    def total_items(self):
        total = 0
        items = self.invoiceitem_set.all()

        for item in items:
            total += item.cost * item.qty

        return total

    def total(self):
        items = self.total_items()
        return items

    def paid(self):
        return self.status == 'Paid'

    def unpaid(self):
        return self.status == 'Unpaid'

    def draft(self):
        return self.status == 'Draft'


class InvoiceItem(models.Model):
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE)
    name = models.CharField(max_length=128)
    description = models.TextField()
    cost = models.DecimalField(decimal_places=2, max_digits=10)
    qty = models.IntegerField()

    def total(self):
        return self.cost * self.qty
