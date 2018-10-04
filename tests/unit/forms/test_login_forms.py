from django.test import TestCase

from users.forms.login_form import LoginForm
from users.models import User


class LoginFormTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username="beefing",
            password="beefingpass",
            email="beef@example.com"
        )
        # self.user.save()

    def test_valid_data_with_username_and_password(self):
        form = LoginForm({
            "username": "beefing",
            "password": "beefingpass"
        })
        self.assertTrue(form.is_bound)
        self.assertTrue(form.is_valid())

    def test_should_validate_empty_form(self):
        form = LoginForm()
        self.assertFalse(form.is_bound)
        self.assertFalse(form.is_valid())

    def test_should_validate_empty_username_and_password_fields(self):
        form = LoginForm({
            "username": "",
            "password": ""
        })
        self.assertTrue(form.is_bound)
        self.assertFalse(form.is_valid())