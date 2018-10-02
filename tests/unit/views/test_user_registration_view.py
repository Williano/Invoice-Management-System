from django.test import TestCase
from django.urls import resolve, reverse

from users.views import registration


class UserRegistrationViewTest(TestCase):

    def test_url_resolves_to_registration_view(self):
        found = resolve('/registration/')
        self.assertEqual(found.func, registration)

    def test_registration_page_returns_correct_html(self):
        response = self.client.get(reverse("users:registration"))
        html = response.content.decode('utf8')

        self.assertIn(response.status_code, [200, 302])
        self.assertIn('Already Have An Account?', html)
        self.assertIn('<title>mPedigree Invoice Manager | Registration</title>', html)

    def test_authenticated_user_redirected_to_dashboard(self):
        pass

    def test_invalid_login_data_returns_with_message(self):
        pass
