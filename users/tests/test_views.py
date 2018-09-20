from django.test import TestCase
from django.urls import reverse

from users.models import User


class UserViewsTest(TestCase):

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

        response = self.client.post(
            reverse("users:registration"),
            {
                'username': "thorloki",
                "first_name": "athena",
                "last_name": "zeus",
                "password": "zeusiskingofthegods",
                "email": "athena@example.com",
                "user_type": "REGULAR"
            }
        )

        self.assertContains(response, "A user with that Email already exist")

        user = User.objects.filter(username="athena").first()

        self.assertIsNotNone(user)
        self.assertEqual(user.username, "athena")
        self.assertEqual(user.email, "athena@example.com")

    def test_invalid_user_data(self):
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

        self.assertIn(response.status_code, [200, 302])

        response = self.client.get(
            reverse("users:registration")
        )

        self.assertIn(response.status_code, [200, 302])
        self.assertContains(response, "Username")
        self.assertContains(response, "Email")
        self.assertContains(response, "Password")

    def test_user_can_log_in(self):
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

        response = self.client.post(
            reverse("users:login"),
            {
                "username": "athena",
                "password": "zeusiskingofthegods"
            }
        )

        self.assertIn(response.status_code, [200, 302])

        response = self.client.post(
            reverse("users:login"),
            {
                "username": "thorloki",
                "password": "godofthunder"
            }
        )

        self.assertIn(response.status_code, [200, 302])
        self.assertContains(response, "Username and/or password does not exist")

        response = self.client.get(
            reverse("users:login")
        )

        self.assertIn(response.status_code, [200, 302])
        self.assertContains(response, "Username")

    def test_user_can_log_out(self):
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

        response = self.client.post(
            reverse("users:login"),
            {
                "username": "athena",
                "password": "zeusiskingofthegods"
            }
        )

        self.assertIn(response.status_code, [200, 302])

        response = self.client.get(
            reverse("users:logout"),
        )

        self.assertIn(response.status_code, [200, 302])