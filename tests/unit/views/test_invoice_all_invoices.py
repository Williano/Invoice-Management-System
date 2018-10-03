from django.test import TestCase
from django.urls import resolve, reverse

from invoice.views import all_invoices
from users.models import User


class InvoiceAllInvoicesViewTest(TestCase):

    def setUp(self):
        User.objects.create_user(
            username="johndoe",
            password="johndoepass",
            email="johndoe@example.com"
        )

        self.client.login(username="johndoe", password="johndoepass")

    def test_url_resolves_to_invoice_view(self):
        found = resolve('/invoice/invoice/all/')
        self.assertEqual(found.func, all_invoices)

    def test_index_page_returns_correct_html(self):
        response = self.client.get(reverse("invoice:all_invoices"))
        html = response.content.decode('utf8')

        self.assertEqual(response.status_code, 200)
        self.assertIn('<title>mPedigree Invoice Manager | All Invoices</title>', html)