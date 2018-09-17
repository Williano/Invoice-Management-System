# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.db.models import Q
from django.shortcuts import render, redirect

from users.forms import RegistrationForm, LoginForm
from users.models import User
from users.utils import validate_data


def registration(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            email = form.cleaned_data["email"]
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            user_type = form.cleaned_data["user_type"]

            ok, msg = validate_data(username, password, email, first_name, last_name, user_type)
            if not ok:
                for m in msg:
                    messages.error(request, m)

                return redirect('users:registration')
            else:
                if User.objects.filter(Q(username__exact=username) | Q(email__exact=email)).first() is None:
                    user = User(
                        username=username, password=password,
                        email=email, first_name=first_name,
                        last_name=last_name, user_type=user_type
                    )
                    user.set_password(password)
                    user.save()

                    # sign them in and redirect to dashboard
                    user = authenticate(username=username, password=password)
                    if user is not None:
                        login(request, user)
                        messages.success(request, "Registration successful")

                        return redirect('users:login')
                    else:
                        # Invalid username and/or password provided
                        messages.info(request, "Username and/or password does not exist")
                        return render(request, "users/registration.html", {
                            'registration_form': form
                        })
                else:
                    # User already exists
                    messages.info(request, "Username and/or email already taken")
                    return render(request, "users/registration.html", {
                        'registration_form': form
                    })
    else:
        form = RegistrationForm()

    return render(request, "users/registration.html", {
        'registration_form': form
    })


def sign_in(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            if username is not None and len(username) > 0:
                user = authenticate(username=username, password=password)
                if user is not None:
                    user.check_password(password)
                    login(request, user)
                    messages.success(request, "You've been successfully logged in! ")
                    return redirect('invoice:index')
                else:
                    messages.info(request, "Username and/or password does not exist")
                    return render(request, "users/login.html", {
                        'login_form': form
                    })
            else:
                messages.info(request, "Please provide a username.")
                return render(request, "users/login.html", {
                    'login_form': form
                })
    else:
        form = LoginForm()

    return render(request, "users/login.html", {
        'login_form': form
    })


def sign_out(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request, 'You have successfully logged out ! Login again')

    return redirect('users:login')
