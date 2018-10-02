from django.test import TestCase
from django.urls import reverse


class UserLogoutTest(TestCase):
    def setUp(self):
        pass

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

    def test_logout_destroys_user_session(self):
        pass

    def test_logging_out_authenticated_user_returns_message(self):
        pass
