import uuid

from django.db import models

from invoice.models.customer import Customer


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
