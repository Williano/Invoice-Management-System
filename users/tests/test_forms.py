from django.test import TestCase

from users.forms import LoginForm, RegistrationForm
from users.models import User


class LoginFormTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username="johdoe", password="johndoepass", email="johdoe@example.com")
        self.user.save()

    def test_valid_data(self):
        form = LoginForm({
            "username": "johdoe",
            "password": "johndoepass"
        })
        self.assertTrue(form.is_bound)
        self.assertTrue(form.is_valid())

        form = LoginForm()
        self.assertFalse(form.is_bound)
        self.assertFalse(form.is_valid())

        form = LoginForm({
            "username": "",
            "password": ""
        })
        self.assertTrue(form.is_bound)
        self.assertFalse(form.is_valid())


class RegistrationFormTest(TestCase):

    def test_valid_bound_data(self):
        form = RegistrationForm({
            'username': "athena",
            "first_name": "athena",
            "last_name": "zeus",
            "password": "zeusiskingofthegods",
            "email": "athena@example.com",
            "user_type": "REGULAR"
        })
        self.assertTrue(form.is_bound)
        self.assertTrue(form.is_valid())

        form = RegistrationForm({
            'username': "",
            "first_name": "athena",
            "last_name": "",
            "password": "",
            "email": "",
            "user_type": "REGULAR"
        })
        self.assertTrue(form.is_bound)
        self.assertFalse(form.is_valid())

        form = RegistrationForm()
        self.assertFalse(form.is_bound)
        self.assertFalse(form.is_valid())