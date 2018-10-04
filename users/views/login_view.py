from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render

from users.forms.login_form import LoginForm


def sign_in(request):
    """Logs the user in

    Retrieves the username and password provided by the
    user after validating the form. The username and
    password is authenticated, and if successful, the
    user is logged into the current session.

    If the authentication fails, or the form data provided
    is invalid, or the data provided already exist, the
    user is presented with the form and the appropriate
    error message.

    :param request: The WSGIRequest object for the current session
    :return HttpResponse:
    """
    if request.method == "POST":
        # Get the login form with the data bound to it
        form = LoginForm(request.POST)

        # check to see if the data provided is valid.
        if form.is_valid():

            # If the data is valid, retrieve it.
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            # check to ensure that the username is not None.
            # If it is, inform the user accordingly and presented
            # with the form to try again
            if username is not None and len(username) >= 6:

                # authenticate the user. If the user object is not None,
                # it means the user exists in the system. Then if the password
                # check passes, the user is logged in and redirected to their
                # dashboard.
                user = authenticate(username=username, password=password)
                if user is not None:
                    user.check_password(password)
                    login(request, user)

                    messages.success(request, "You've been successfully logged in! ")
                    return redirect('invoice:index')
                else:
                    messages.warning(request, "Username and/or password does not exist")
        else:
            messages.warning(request, "Username and/or password contains invalid data")
    else:
        if request.user.is_authenticated:
            return redirect('invoice:index')

        # For a GET request, create a login form ad pass it
        # to the login page for rendering.
        form = LoginForm()

    # render the login page along with the form
    return render(request, "users/login.html", {
        'login_form': form,
        'title': 'Sign In'
    })