# Third Party imports.
from django.test import TestCase

# Local applications imports.
from invoice.forms import CustomerForm


class CustomerFormTest(TestCase):

    def test_form_with_valid_data(self):
        form = CustomerForm({
            'name': 'mPedigree',
            'address': 'P.O.Box KS 10731',
            'city': "Accra",
            'region': "Greater",
            'country': "Ghana",
            'email': "info@gmail.com",
        })

        self.assertTrue(form.is_valid(), msg=str(form.cleaned_data))
        self.assertTrue(form.is_bound)
        self.assertEqual(form.cleaned_data['name'], u'mPedigree')
        self.assertEqual(form.cleaned_data['address'], u'P.O.Box KS 10731')
        self.assertEqual(form.cleaned_data['city'], u'Accra')
        self.assertEqual(form.cleaned_data['region'], u'Greater')
        self.assertEqual(form.cleaned_data['country'], u'Ghana')

    def test_blank_form(self):
        form = CustomerForm()

        self.assertFalse(form.is_bound)
        self.assertFalse(form.is_valid())

    def test_form_with_name_field_left_blank(self):
        form = CustomerForm({
            'name': '',
        })

        self.assertTrue(form.is_bound)
        self.assertFalse(form.is_valid())
