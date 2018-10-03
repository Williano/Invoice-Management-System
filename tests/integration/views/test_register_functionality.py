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
        self.client.post(
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

        user = User.objects.filter(username="athena").first()

        self.assertIsNotNone(user)
        self.assertEqual(user.username, "athena")
        self.assertEqual(user.email, "athena@example.com")

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

        self.assertIn(response.status_code, [302])
        self.assertIn(response.content, "")
        self.assertTrue(response.url, "/registration/")

    def test_authenticated_user_redirected_to_dashboard(self):
        login = self.client.login(username="johndoe", password="johndoepass")
        self.assertTrue(login)

        response = self.client.get(reverse("users:registration"))
        found = resolve(response.url)
        self.assertEqual(found.func, index)

    def test_registration_with_existing_email(self):
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

        self.assertIn(response.status_code, [200, 302])

