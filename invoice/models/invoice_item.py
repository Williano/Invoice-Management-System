from django.db import models

from invoice.models.inv import Invoice


class InvoiceItem(models.Model):
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE)
    name = models.CharField(max_length=128)
    description = models.TextField()
    cost = models.DecimalField(decimal_places=2, max_digits=10)
    qty = models.IntegerField()

    def __str__(self):
        return self.name

    def total(self):
        return self.cost * self.qty
