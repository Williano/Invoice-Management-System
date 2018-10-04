from django.forms import ModelForm
from django import forms

from users.models import User


class RegistrationForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        self.fields['email'].required = True
        self.fields['email'].unique = True

        self.fields['password'].required = True

        self.fields['username'].required = True
        self.fields['username'].unique = True

        self.fields['first_name'].required = True
        self.fields['last_name'].required = True

    class Meta:
        model = User
        fields = ['username', 'password', 'first_name', 'last_name', 'email', 'user_type']
        widgets = {
            'password': forms.PasswordInput,
            'email': forms.EmailInput,
        }
        help_texts = {
            'password': '* Password must be at least 6 characters long',
            'username': '* Username must be blah blah blah',
        }