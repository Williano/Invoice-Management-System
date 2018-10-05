from django.http import HttpResponseRedirect
from django.test import TestCase, Client
from django.urls import reverse, resolve

from invoice.models.customer import Customer
from invoice.views import customer_list


class CustomerCreationTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_should_create_new_customer_after_login(self):
        response = self.client.post(
            reverse("users:registration"),
            {
                'username': "athena",
                "first_name": "athena",
                "last_name": "zeus",
                "password": "zeusiskingofthegods",
                "email": "athena@example.com",
                "user_type": "REGULAR"
            }
        )

        self.assertEqual(response.url, "/invoice/")

        response = self.client.post(
            reverse("invoice:new_customer"),
            {
                'name': "John Mahana",
                "address": "Lapaz",
                "city": "Accra",
                "region": "GA",
                "country": "Ghana",
                "email": "some@some.com"
            }
        )

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.__class__.__name__, HttpResponseRedirect.__name__)
        self.assertEqual("utf-8", response.charset)
        self.assertEqual(response.url, reverse("invoice:customer_list"))

        customers = Customer.objects.all()
        self.assertEqual(1, customers.count())
        customer = Customer.objects.filter(name="John Mahana")
        self.assertEqual(len(customer), 1)

    def test_should_create_new_customer_without_login(self):
        response = self.client.post(
            reverse("invoice:new_customer"),
            {
                'name': "Thor Odinson",
                "address": "Asgard",
                "city": "Accra",
                "region": "GA",
                "country": "Ghana",
                "email": "odinson@example.com"
            }
        )

        self.assertEqual(response.status_code, 302)
        self.assertIn(response.url, "/?next=/invoice/customer/new/")
        self.assertTrue(len(response.templates) == 0)
        self.assertIn(response.wsgi_request.scheme, response.allowed_schemes)

    def test_should_create_new_customer_with_only_name_and_address(self):
        response = self.client.post(
            reverse("users:registration"),
            {
                'username': "athena",
                "first_name": "athena",
                "last_name": "zeus",
                "password": "zeusiskingofthegods",
                "email": "athena@example.com",
                "user_type": "REGULAR"
            }
        )

        self.assertEqual(response.url, "/invoice/")

        user_login = self.client.login(username="athena", password="zeusiskingofthegods")
        self.assertTrue(user_login)

        response = self.client.post(
            reverse("invoice:new_customer"),
            {
                'name': "Thor Odinson",
                "address": "Asgard",
                "city": "",
                "region": "",
                "country": "",
                "email": ""
            }
        )

        self.assertEqual(response.status_code, 302)
        self.assertIn(response.url, "/invoice/customers/")
        self.assertEqual(resolve(response.url).func, customer_list)
        self.assertTrue(len(response.templates) == 0)
        self.assertIn(response.wsgi_request.scheme, response.allowed_schemes)
