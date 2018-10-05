# Third party imports.
from django.test import TestCase

# Local application imports
from invoice.models.customer import Customer
from invoice.models.inv import Invoice
from invoice.models.invoice_item import InvoiceItem


# models test
class InvoiceModelTest(TestCase):
    def setUp(self):
        customer1 = Customer.objects.create(
            name="Mpedigree",
            address="P.O.Box KS 10731",
            city="Kumasi",
            region="AH",
            country="Ghana",
            email="paawilly17@gmail.com",
        )

        customer2 = Customer.objects.create(
            name="JimahTech",
            address="P.O.Box KS 10731",
            city="Kumasi",
            region="AH",
            country="00233",
            email="paawilly18@gmail.com",
        )

        invoice1 = Invoice.objects.create(
            customer=customer1,
            invoice_code="b0aa7e49-8565-42c6-856b-4f1b03205d77",
            valid=True,
            date_created="09-28-2018",
            expiration_date="2018-09-29",
            status="Unpaid",


        )

        invoice2 = Invoice.objects.create(
            customer=customer2,
            invoice_code="b0aa7e49-8565-42c6-856b-4f1b03205d88",
            valid=True,
            date_created="2018-09-29",
            expiration_date="2018-10-29",
            status="Paid",


        )

        InvoiceItem.objects.create(
            invoice=invoice1,
            name="Software Books",
            description="new item for business2",
            cost=50,
            qty=20
        )

        InvoiceItem.objects.create(
            invoice=invoice1,
            name="Software",
            description="new item for business",
            cost=50,
            qty=20
              )

        InvoiceItem.objects.create(
            invoice=invoice2,
            name="Software come",
            description="new item for business3",
            cost=20,
            qty=20
              )

    def test_customer_name(self):
        customer = Customer.objects.get(id=1)
        expected_object_name = "%s" % customer.name
        self.assertEquals(expected_object_name, customer.__str__())

    def test_invoice_id(self):
        invoice = Invoice.objects.get(id=1)
        expected_object_name = "%s" % invoice.id
        self.assertEquals(expected_object_name, invoice.__str__())

    def test_total_price_for_invoice_item_one(self):
        invoice_item = InvoiceItem.objects.get(id=1)
        self.assertEqual(invoice_item.total(), 1000)

    def test_total_price_for_invoice_item_two(self):
        invoice_item = InvoiceItem.objects.get(id=3)
        self.assertEqual(invoice_item.total(), 400)

    def test_total_items_in_an_invoice(self):
        invoice = Invoice.objects.get(id=1)
        invoice_item = invoice.invoiceitem_set.all().count()
        self.assertEqual(invoice_item, 2)

    def test_total_cost_of_an_invoice(self):
        invoice = Invoice.objects.get(id=1)
        self.assertEqual(invoice.total(), 2000)
