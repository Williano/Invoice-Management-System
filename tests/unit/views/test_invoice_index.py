from django.test import TestCase
from django.urls import resolve, reverse

from invoice.views import index
from users.models import User


class InvoiceIndexViewTest(TestCase):

    def setUp(self):
        User.objects.create_user(
            username="johndoe",
            password="johndoepass",
            email="johndoe@example.com"
        )

        self.client.login(username="johndoe", password="johndoepass")

    def test_url_resolves_to_invoice_view(self):
        found = resolve('/invoice/')
        self.assertEqual(found.func, index)

    def test_index_page_returns_correct_html(self):
        response = self.client.get(reverse("invoice:index"))
        html = response.content.decode('utf8')

        self.assertEqual(response.status_code, 200)
        self.assertIn('<title>mPedigree Invoice Manager | Recent Invoices</title>', html)

    def test_index_page_works_correctly_with_invalid_page_number(self):
        response = self.client.get(reverse("invoice:index"), {'page': 'foo'})
        html = response.content.decode('utf8')

        self.assertEqual(response.status_code, 200)
        self.assertIn('<title>mPedigree Invoice Manager | Recent Invoices</title>', html)