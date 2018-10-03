from django.test import TestCase
from django.urls import reverse, resolve

from invoice.views import index
from users.models import User


class UserLoginTest(TestCase):

    def setUp(self):
        User.objects.create_user(
            username="athena",
            password="zeusiskingofthegods",
            email="athena@example.com",
        )

    def test_user_can_log_in(self):

        response = self.client.post(
            reverse("users:login"),
            {
                "username": "athena",
                "password": "zeusiskingofthegods"
            }
        )

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, "/invoice/")
        self.assertEqual(resolve("/invoice/").func, index)

    def test_authenticated_user_redirected_to_invoice(self):
        self.client.login(username="athena", password="zeusiskingofthegods")
        response = self.client.get(reverse("users:login"))

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, "/invoice/")
        self.assertEqual(resolve("/invoice/").func, index)

    def test_login_with_invalid_credentials(self):
        response = self.client.post(
            reverse("users:login"),
            {
                "username": "thorloki",
                "password": "godofthunder"
            }
        )

        self.assertEqual(response.status_code, 200)
        self.assertIn("<title>mPedigree Invoice Manager | Sign In</title>", response.content)
        self.assertIn("Username and/or password does not exist", response.content)

    def test_login_with_credentials_that_dont_meet_requirements(self):
        response = self.client.post(
            reverse("users:login"),
            {
                "username": "tho",
                "password": "god"
            }
        )

        self.assertEqual(response.status_code, 200)
        self.assertIn("<title>mPedigree Invoice Manager | Sign In</title>", response.content)
        self.assertIn("Username and/or password contains invalid data", response.content)
