from datetime import date
from decimal import Decimal

from django.test import TestCase, Client
from django.urls import reverse, resolve

from users.models import User
from invoice.models.customer import Customer
from invoice.models.inv import Invoice
from invoice.models.invoice_item import InvoiceItem


class InvoiceCreationTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        # creat user
        User.objects.create_user(
            username="janedoe",
            password="janedoepass",
            email="janedoe@example.com"
        )

        # create a customer
        cls.customer = Customer(
            name='jojo',
            address='4555 street',
            city='Kumasi',
            region='AR',
            country="Ghana",
            email='jojo@example.com'
        )

        cls.customer.save()



    def setUp(self):
        self.client = Client()
        self.client.login(username='janedoe', password='janedoepass')

    def tearDown(self):
        self.client.logout()

    def test_should_create_an_invoice(self):
        customer = Customer.objects.filter(name=InvoiceCreationTest.customer.name).first()

        response = self.client.post(reverse('invoice:new_invoice'), {
            'customer_id': customer.id,
            'expiration_date': date.today(),
            'status': 'Unpaid'
        })

        self.assertEqual(response.url, '/invoice/invoice/1/')
        self.assertEqual(response.status_code, 302)

        invoice = Invoice.objects.filter(id=InvoiceCreationTest.customer.id).first()
        self.assertTrue( invoice.unpaid() )
        self.assertEqual( invoice.expiration_date, date.today())

    def test_should_create_an_invoice_and_add_5_invoice_items(self):
        customer = Customer.objects.filter(name=InvoiceCreationTest.customer.name).first()

        response = self.client.post(reverse('invoice:new_invoice'), {
            'customer_id': customer.id,
            'expiration_date': date.today(),
            'status': 'Unpaid'
        })

        self.assertEqual(response.url, '/invoice/invoice/1/')
        self.assertEqual(response.status_code, 302)
        
        #get the invoice
        invoice = Invoice.objects.filter(id=InvoiceCreationTest.customer.id).first()
        self.assertEqual(invoice.id, 1)
        
        #add 5 items
        response = self.client.post(reverse('invoice:add_item', args=(invoice.id,)), {
            'form-TOTAL_FORMS': 5,
            'form-INITIAL_FORMS': 0,
            'form-MIN_NUM_FORMS': 0,
            'form-MAX_NUM_FORMS': 100,
            'form-0-item': 'Car',
            'form-0-description': 'Jeep',
            'form-0-cost': Decimal(50000),
            'form-0-qty': 5,
            'form-1-item': 'House',
            'form-1-description': 'Flat',
            'form-1-cost': Decimal(100000),
            'form-1-qty': 4,
            'form-2-item': 'Office',
            'form-2-description': 'Flat',
            'form-2-cost': Decimal(105000),
            'form-2-qty': 6,
            'form-3-item': 'Pen',
            'form-3-description': 'Big Pen',
            'form-3-cost': Decimal(1),
            'form-3-qty': 4,
            'form-4-item': 'Computer',
            'form-4-description': 'Mac book',
            'form-4-cost': Decimal(2000),
            'form-4-qty': 8
        })

        invoice_items = invoice.invoiceitem_set.all()
        
        expected_total_cost = 5 * Decimal(50000) + 4 * Decimal(100000) + 6 * Decimal(105000) + 4* Decimal(1) + 8 * Decimal(2000)

        self.assertEqual(invoice.total_items(), expected_total_cost)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(len(invoice_items), 5)

    def test_should_create_an_invoice_and_adding_items_using_invalid_formset(self):
        customer = Customer.objects.filter(name=InvoiceCreationTest.customer.name).first()

        response = self.client.post(reverse('invoice:new_invoice'), {
            'customer_id': customer.id,
            'expiration_date': date.today(),
            'status': 'Unpaid'
        })

        self.assertEqual(response.url, '/invoice/invoice/1/')
        self.assertEqual(response.status_code, 302)
            
        #get the invoice
        invoice = Invoice.objects.filter(id=InvoiceCreationTest.customer.id).first()
        self.assertEqual(invoice.id, 1)
            
        #add 3 items
        response = self.client.post(reverse('invoice:add_item', args=(invoice.id,)), {
            'form-TOTAL_FORMS': 3,
            'form-INITIAL_FORMS': 0,
            'form-MIN_NUM_FORMS': 0,
            'form-MAX_NUM_FORMS': 100,
            'form-0-item': 'Car',
            'form-0-description': None,
            'form-0-cost': None,
            'form-0-qty': 5,
            'form-1-item': 'House',
            'form-1-description': 'Flat',
            'form-1-cost': Decimal(100000),
            'form-1-qty': 4,
            'form-2-item': 'Office',
            'form-2-description': 'Flat',
            'form-2-cost': Decimal(105000),
            'form-2-qty': 6,
        })

        invoice_items = invoice.invoiceitem_set.all()
            
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(invoice_items), 0)