from django.test import TestCase
from django.utils import timezone
from django.core.urlresolvers import reverse
from invoice.models.customer import Customer
from invoice.models.inv import Invoice
from invoice.models.invoice_item import InvoiceItem


# models test
class InvoiceModelTest(TestCase):
    def setUp(self):
        c1 = Customer.objects.create(
            name="Mpedigree",
            address1="P.O.Box KS 10731",
            address2="Adum",
            city="Kumasi",
            state="AH",
            zip="00233",
            email="paawilly17@gmail.com",
        )

        c2 = Customer.objects.create(
            name="JimahTech",
            address1="P.O.Box KS 10731",
            address2="Adum",
            city="Kumasi",
            state="AH",
            zip="00233",
            email="paawilly18@gmail.com",
        )

        inv1 = Invoice.objects.create(
            customer=c1,
            invoice_code="b0aa7e49-8565-42c6-856b-4f1b03205d77",
            valid=True,
            date_created="09-28-2018",
            expiration_date="2018-09-29",
            status="unpaid",


        )

        inv2 = Invoice.objects.create(
            customer=c2,
            invoice_code="b0aa7e49-8565-42c6-856b-4f1b03205d88",
            valid=True,
            date_created="2018-09-29",
            expiration_date="2018-10-29",
            status="paid",


        )

        InvoiceItem.objects.create(
            invoice=inv1,
            name="Software Books",
            description="new item for business2",
            cost=50,
            qty=20
        )

        InvoiceItem.objects.create(
            invoice=inv1,
            name="Software",
            description="new item for business",
            cost=50,
            qty=20
              )

        InvoiceItem.objects.create(
            invoice=inv2,
            name="Software come",
            description="new item for business3",
            cost=20,
            qty=20
              )

    def test_customer_content(self):
        customer = Customer.objects.get(id=1)
        expected_object_name = "%s" % customer.name
        self.assertEquals(expected_object_name, customer.__str__())

    def test_customer_content_with_invalid_name(self):
        customer = Customer.objects.get(id=2)
        expected_object_name = "%s" % customer.name
        self.assertEquals(expected_object_name, customer.__str__())

    def test_invoice_content(self):
        invoice = Invoice.objects.get(id=1)
        expected_object_name = "%s" % invoice.id
        self.assertEquals(expected_object_name, invoice.__str__())

    def test_invoice_content_with_invalid_name(self):
        invoice = Invoice.objects.get(id=2)
        expected_object_name = "%s" % invoice.id
        self.assertEquals(expected_object_name, invoice.__str__())

    def test_invoice_item_one_total_price(self):

        invoice_item = InvoiceItem.objects.get(id=1)
        total_price = invoice_item.cost * invoice_item.qty
        self.assertEqual(total_price, 1000)

    def test_invoice_item_two_total_price(self):
        invoice_item = InvoiceItem.objects.get(id=3)
        total_price = invoice_item.cost * invoice_item.qty
        self.assertEqual(total_price, 400)

    def test_unpaid_invoice(self):
        invoice_unpaid = Invoice.objects.filter(status="unpaid").count()
        self.assertEqual(invoice_unpaid, 1)
