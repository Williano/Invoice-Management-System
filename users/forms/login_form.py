from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(
        min_length=6,
        max_length=80,
        label="Username",
        required=True
    )

    password = forms.CharField(
        widget=forms.PasswordInput,
        label="Password",
        required=True
    )