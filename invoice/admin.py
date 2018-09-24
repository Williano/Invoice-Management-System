from django.contrib import admin

# Register your models here.
from invoice.models.invoice_item import InvoiceItem
from invoice.models.customer import Customer
from invoice.models.inv import Invoice

admin.site.register(Customer)
admin.site.register(Invoice)
admin.site.register(InvoiceItem)
