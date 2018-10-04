from django.test import TestCase, Client
from django.urls import reverse, resolve

from invoice.views import index
from users.models import User


class UserRegistrationTest(TestCase):

    def setUp(self):
        User.objects.create_user(
            username="johndoe",
            password="johndoepass",
            email="johndoe@example.com"
        )

        self.client = Client()

    def test_user_can_register(self):
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

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, "/invoice/")
        self.assertEqual(resolve("/invoice/").func, index)

        user = User.objects.filter(username="athena").first()

        self.assertIsNotNone(user)
        self.assertEqual(user.username, "athena")
        self.assertEqual(user.email, "athena@example.com")

        # Test: registering with existing email address
        response = self.client.post(
            reverse("users:registration"),
            {
                'username': "thorloki",
                "first_name": "thor",
                "last_name": "loki",
                "password": "zeusiskingofthegods",
                "email": "athena@example.com",
                "user_type": "REGULAR"
            }
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual("utf-8", response.charset)
        self.assertIn("<title>mPedigree Invoice Manager | Registration</title>", response.content)
        self.assertEqual(User.objects.filter(email="athena@example.com").count(), 1)
        self.assertIn("A user with that Email already exist", response.content)

    def test_should_reject_registration_with_all_invalid_fields(self):
        response = self.client.post(
            reverse("users:registration"),
            {
                'username': "we",
                "first_name": "ae",
                "last_name": "er",
                "password": "df",
                "email": "re@dc.co",
                "user_type": "SELECT"
            }
        )

        self.assertEqual(response.status_code, 302)
        self.assertIn(response.content, "")
        self.assertTrue(response.url, "/registration/")

    def test_authenticated_user_redirected_to_dashboard(self):
        login = self.client.login(username="johndoe", password="johndoepass")
        self.assertTrue(login)
        
        response = self.client.get(reverse("users:registration"))
        found = resolve(response.url);
        self.assertEqual(found.func, index)

