# Third party imports.
from django.db import models


class Customer(models.Model):
    """
       Models for a customer.
    """

    name = models.CharField(max_length=256, null=False, blank=False,
                            help_text='Enter Customer or Company')
    address = models.CharField(max_length=100, null=True, blank=True,
                               help_text='Enter address of customer or Company'
                               )
    city = models.CharField(max_length=100, null=True, blank=True,
                            help_text='Enter the city of the address')
    region = models.CharField(max_length=50, null=True, blank=True,
                              help_text='Enter the region of the address')
    country = models.CharField(max_length=100, null=True, blank=True,
                               help_text='Enter the country of the address')
    email = models.EmailField(null=True, blank=True,
                              help_text='Enter the email of the customer or \
                              Company')

    def __str__(self):
        """
           Displays a human-readable representation of Customer Model
        """
        return self.name

    def invoices(self):
        """
           Returns all the invoices of a customer.
        """
        from invoice.models.inv import Invoice

        return Invoice.objects.filter(customer=self).count()

