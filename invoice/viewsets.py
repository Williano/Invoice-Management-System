# Third Party imports.
from rest_framework import viewsets, filters

# Local application imports.
from invoice.models.inv import Invoice
from .serializers import InvoiceSerializer


class InvoiceViewSet(viewsets.ModelViewSet):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('id', 'customer__name', 'valid',)
