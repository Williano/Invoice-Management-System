import re


def validate_data(username, password, email, first_name, last_name, user_type):
    ok, messages = True, []

    if first_name is None or len(first_name) < 1:
        messages.append("Provide first name")
        ok = False

    if last_name is None or len(last_name) < 1:
        messages.append("Provide last name")
        ok = False

    if username is None or len(username) < 3:
        messages.append("Username is required and must be at least 3 characters long")
        ok = False

    if password is None or len(password) < 6:
        messages.append("Password is required and must be at least 6 characters long")
        ok = False

    if not re.match(r"^[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]*$", email):
        messages.append("Invalid Email Address")
        ok = False

    if user_type == 'SELECT':
        messages.append('Please select the applicable user type')
        ok = False

    return ok, messages

