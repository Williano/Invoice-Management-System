from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render

from users.forms.registration_form import RegistrationForm
from users.models import User
from users.utils import validate_data


def registration(request):
    """Register a new account

    Retrieves the registration information submitted by the user if
    the form is bound and valid. The next step is to call the
    ` validate_data()` function to ensure that the information provided
    has passed the necessary requirements to be used. Otherwise the user
    is presented with an error message and the form to try again.

    If the data is valid, we create a new user object with the data and
    save it in the database. The user is then automatically logged in
    and redirected to their dashboard.

    In all instances where the data is not valid, the user is presented
    with the form and the appropriate messages to try again.

    :param request: The WSGIRequest object for the current session
    :return HttpResponse:
    """
    if request.method == 'POST':

        # Bind the form with the data submitted and check to
        # see if the data is valid.
        form = RegistrationForm(request.POST)
        if form.is_valid():

            # retrieve the valid data
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            email = form.cleaned_data["email"]
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            user_type = form.cleaned_data["user_type"]

            # validate the information provided by the user. If there is
            # some invalid data, redirect to the registration page with
            # the error messages
            ok, msg = validate_data(username, password, email, first_name, last_name, user_type)
            if not ok:
                for m in msg:
                    messages.warning(request, m)

                return redirect('users:registration')
            else:
                # Ensure that the username provided is unique. If so, create and
                # save a new user instance
                if User.objects.filter(email__exact=email).first() is None:
                    user = User(
                        username=username, password=password,
                        email=email, first_name=first_name,
                        last_name=last_name, user_type=user_type
                    )
                    user.set_password(password)
                    user.save()

                    # sign them in and redirect to dashboard after authentication
                    user = authenticate(username=username, password=password)
                    if user is not None:
                        login(request, user)
                        messages.success(request, "Registration successful! Welcome %s !" %user.username)

                        return redirect('invoice:index')
                else:
                    # User already exists
                    messages.warning(request, "A user with that Email already exist")
                    return render(request, "users/registration.html", {
                        'registration_form': form,
                        'title': 'Registration'
                    })
    else:
        if request.user.is_authenticated:
            return redirect('invoice:index')

        # For a GET request, create a registration form ad pass it
        # to the login page for rendering.
        form = RegistrationForm()

    return render(request, "users/registration.html", {
        'registration_form': form,
        'title': 'Registration'
    })
