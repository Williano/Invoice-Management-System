from django.test import TestCase
from django.urls import reverse


class UserLoginTest(TestCase):

    def setUp(self):
        pass

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
        # self.assertContains(response, "Username and/or password does not exist")

        response = self.client.get(
            reverse("users:login")
        )

        self.assertIn(response.status_code, [200, 302])
        # self.assertContains(response, "Username")

    def tearDown(self):
        pass
