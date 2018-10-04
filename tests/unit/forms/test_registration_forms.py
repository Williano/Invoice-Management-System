from unittest import TestCase

from users.forms.registration_form import RegistrationForm


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