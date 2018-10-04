from django.contrib import messages
from django.contrib.auth import logout
from django.shortcuts import redirect


def sign_out(request):
    """Logs out the currently logged in user

    Destroys the current user session and redirects
    the user to the login page. If the user is not
    logged in for some reason, they are simply redirected
    to the login page.

    It also sends a message along with the response,
    telling the user about the success or failure of
    their request.

    :param request: The WSGIRequest object for the current session
    :return: HttpResponse: Redirects the user to the login page
    """
    if request.user.is_authenticated:
        logout(request)
        messages.success(request, 'You have successfully logged out! Login again!')

    return redirect('users:login')