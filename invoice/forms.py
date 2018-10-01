from __future__ import unicode_literals

from django import forms
from django.forms import formset_factory


class ItemForms(forms.Form):
    item = forms.CharField(min_length=2, max_length=100, widget=forms.TextInput(attrs={'class':'form-control'}))
    description = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    cost = forms.DecimalField(widget=forms.TextInput(attrs={'placeholder':'0.00', 'class': 'form-control' }))
    qty = forms.IntegerField(min_value=1)


ItemFormset = formset_factory(ItemForms, extra=1)