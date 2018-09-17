from django.test import TestCase
from django.urls import reverse

from users.models import User


class UserViewsTest(TestCase):

    def test_user_can_register(self):
        response = self.client.post(
            reverse("registration"),
            {
                'username': "athena",
                "first_name": "athena",
                "last_name": "zeus",
                "password": "zeusiskingofthegods",
                "email": "athena@example.com"
             }
        )

        self.assertEqual(response.status_code, 200)

        user = User.objects.get(username="athena")

        self.assertIsNotNone(user)
        self.assertEqual(user.username, "athena")
        self.assertEqual(user.email, "athena@example.com")