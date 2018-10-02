from django.test import TestCase
from django.urls import reverse

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

        self.assertIn(response.status_code, [200, 302])

        response = self.client.post(
            reverse("users:login"),
            {
                "username": "thorloki",
                "password": "godofthunder"
            }
        )

        self.assertIn(response.status_code, [200, 302])
        # self.assertContains(response, "Username and/or password does not exist")
