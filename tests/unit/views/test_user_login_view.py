from django.test import TestCase
from django.urls import resolve, reverse

from users.views.login_view import sign_in


class UserLoginViewTest(TestCase):
    def test_url_resolves_to_login_view(self):
        found = resolve('/')
        self.assertEqual(found.func, sign_in)

    def test_login_page_returns_correct_html(self):
        response = self.client.get(reverse("users:login"))
        html = response.content.decode('utf8')

        self.assertIn(response.status_code, [200, 302])
        self.assertIn('Need An Account?', html)
        self.assertIn('Sign Up Now', html)
        self.assertIn('<title>mPedigree Invoice Manager | Sign In</title>', html)