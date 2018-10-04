from __future__ import unicode_literals

from django import forms
from django.forms import formset_factory
from .models.customer import Customer


class CustomerForm(forms.ModelForm):
    """
        Forms for creating a new customer.
    """
    class Meta:
        model = Customer
        fields = ['name', 'address', 'city', 'region', 'country', 'email', ]
        widgets = {'name': forms.TextInput(attrs={"class": "form-control"}),
                   'address': forms.TextInput(attrs={"class": "form-control"}),
                   'city': forms.TextInput(attrs={"class": "form-control"}),
                   'region': forms.TextInput(attrs={"class": "form-control"}),
                   'country': forms.TextInput(attrs={"class": "form-control"}),
                   'email': forms.TextInput(attrs={"class": "form-control"}),
                   }


class ItemForms(forms.Form):
    item = forms.CharField(min_length=2, max_length=100, widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    description = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    cost = forms.DecimalField(
        widget=forms.TextInput(
            attrs={'placeholder': '0.00', 'class': 'form-control' }))
    qty = forms.IntegerField(min_value=1)


ItemFormset = formset_factory(ItemForms, extra=1, min_num=0, max_num=100)