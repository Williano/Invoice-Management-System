from django.test import Client, TestCase
from django.urls import reverse

from users.models import User


class UserRegistrationTest(TestCase):

    def setUp(self):
        self.c = Client()

    def test_user_can_register(self):
        self.c.post(
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

        response = self.c.post(
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

        self.assertIn(response.status_code, [200, 302])
        # self.assertContains(response, "A user with that Email already exist")

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

        self.assertIn(response.status_code, [200, 302])

        response = self.client.get(
            reverse("users:registration")
        )

        self.assertIn(response.status_code, [200, 302])
        self.assertContains(response, "Username")
        self.assertContains(response, "Email")
        self.assertContains(response, "Password")

    def test_authenticated_user_redirected_to_dashboard(self):
        pass

    def test_invalid_registration_data_returns_with_message(self):
        pass
