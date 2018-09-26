# Third party imports.
from rest_framework import routers

# Local application imports.
from invoice.viewsets import InvoiceViewSet


router = routers.DefaultRouter()

router.register(r'invoice', InvoiceViewSet)
