from django.test import TestCase
from django.urls import resolve, reverse

from users.models import User
from users.views.logout_view import sign_out
from users.views.login_view import sign_in


class UserLogoutViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            email="ant@example.com",
            password="antpass",
            username="ant"
        )

    def test_url_resolves_to_logout_view(self):
        found = resolve('/logout/')
        self.assertEqual(found.func, sign_out)

    def test_logout_redirects_to_login_page(self):
        user_login = self.client.login(username="ant", password="antpass")
        self.assertTrue(user_login)

        response = self.client.get(reverse("users:logout"))
        found = resolve(response.url)
        self.assertEqual(found.func, sign_in)
