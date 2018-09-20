import re


def validate_data(username, password, email, first_name, last_name, user_type):
    """Validate the user data provided

    Checks the user information provided during registration
    to ensure that the information is in the appropriate
    format before proceeding.

    :param username: username of the potential
    :param password: password of the potential
    :param email: email address of the potential
    :param first_name: first name of the potential
    :param last_name: last name of the potential
    :param user_type: authorization access of the potential
    :return ok: boolean indicating whether or not there is invalid data
            msg: list of messages to be sent to the user if there were errors
    """
    ok, messages = True, []

    if first_name is None or len(first_name) < 3:
        messages.append("Provide first name")
        ok = False

    if last_name is None or len(last_name) < 3:
        messages.append("Provide last name")
        ok = False

    if username is None or len(username) < 3:
        messages.append("Username is required and must be at least 3 characters long")
        ok = False

    if password is None or len(password) < 8:
        messages.append("Password is required and must be at least 6 characters long")
        ok = False

    if len(email) < 10 or not re.match(r"^[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]*$", email):
        messages.append("Invalid Email Address")
        ok = False

    if user_type == 'SELECT':
        messages.append('Please select the applicable user type')
        ok = False

    return ok, messages

