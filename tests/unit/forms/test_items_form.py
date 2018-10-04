from django.test import TestCase
from decimal import Decimal

from invoice.forms import ItemForms, ItemFormset

class ItemsFormTest(TestCase):
    
    def test_form_with_invalid_data(self):
        form = ItemForms({
            'item' : 452,
            'description' : 452554,
            'cost': "item cost",
            'qty' : "item quantity" 
        })

        self.assertTrue( form.is_bound )
        self.assertFalse( form.is_valid() )
        self.assertEqual(form.errors, {
            'cost': [u'Enter a number.'],
            'qty': [u'Enter a whole number.']
        })

    def test_form_with_valid_data(self):
        form = ItemForms({
            'item': 'Car',
            'description': 'Jeep',
            'cost': Decimal(20000),
            'qty': 2
        })

        self.assertTrue( form.is_valid(), msg=str(form.cleaned_data))
        self.assertTrue( form.is_bound )
        self.assertEqual( form.cleaned_data['item'], u'Car' )
        self.assertEqual( form.cleaned_data['description'], u'Jeep' )
        self.assertEqual( form.cleaned_data['cost'], Decimal(20000) )
        self.assertEqual( form.cleaned_data['qty'], 2 )

    def test_blank_form(self):
        form = ItemForms()

        self.assertFalse( form.is_bound )
        self.assertFalse( form.is_valid() )

    def test_form_some_fields_left_blank(self):
        form = ItemForms({
            'item': 'House',
            'description': "",
            'cost': Decimal(2000),
        })

        self.assertTrue( form.is_bound )
        self.assertFalse( form.is_valid() )


class ItemFormsetTest(TestCase):
    
    def test_formset_has_valid_data(self):
        form = ItemFormset({
            'form-TOTAL_FORMS': 2,
            'form-INITIAL_FORMS': 0,
            'form-MIN_NUM_FORMS': 0,
            'form-MAX_NUM_FORMS': 100,
            'form-0-item': 'Car',
            'form-0-description': 'Jeep',
            'form-0-cost': Decimal(50000),
            'form-0-qty': 5
        })

        self.assertTrue( form.is_bound )
        self.assertTrue( form.is_valid() )

    def test_formset_with_multiple_forms_having_valid_data(self):
        form = ItemFormset({
            'form-TOTAL_FORMS': 2,
            'form-INITIAL_FORMS': 0,
            'form-MIN_NUM_FORMS': 0,
            'form-MAX_NUM_FORMS': 100,
            'form-0-item': 'Car',
            'form-0-description': 'Jeep',
            'form-0-cost': Decimal(50000),
            'form-0-qty': 5,
            'form-1-item': 'House',
            'form-1-description': 'Flat',
            'form-1-cost': Decimal(100000),
            'form-1-qty': 4
        })

        self.assertTrue( form.is_valid() )

    def test_formset_has_invalid_data(self):
        form = ItemFormset({
            'form-TOTAL_FORMS': 1,
            'form-INITIAL_FORMS': 0,
            'form-MIN_NUM_FORMS': 0,
            'form-MAX_NUM_FORMS': 100,
            'form-0-item': 52,
            'form-0-description': Decimal(75),
            'form-0-cost': "Togo",
            'form-0-qty': "merge"
        })

        self.assertTrue( form.is_bound )
        self.assertFalse( form.is_valid() )


    def test_formset_is_blank(self):
        form = ItemFormset()
        self.assertFalse( form.is_bound )
        self.assertFalse( form.is_valid() )