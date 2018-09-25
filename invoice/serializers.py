# Third party imports.
from rest_framework import serializers

# Local application imports.
from .models import Invoice


class InvoiceSerializer(serializers.ModelSerializer):
    total = serializers.ReadOnlyField()

    class Meta:
        model = Invoice
        fields = '__all__'

