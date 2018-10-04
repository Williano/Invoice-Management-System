from django.test import TestCase
from django.urls import resolve, reverse

from users.views.registration_view import registration


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

    def test_should_return_page_with_registration_form_elements(self):
        response = self.client.get(reverse("users:registration"))

        self.assertIn(response.status_code, [200])
        self.assertContains(response, "Username")
        self.assertContains(response, "Email")
        self.assertContains(response, "Password")

