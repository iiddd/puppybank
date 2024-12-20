from django.shortcuts import redirect
from functools import wraps
from django.conf import settings

# Assuming you store the correct token in settings.py
# If not, you can define it directly or retrieve it from the database or an environment variable.
EXPECTED_TOKEN = getattr(settings, 'STATIC_AUTH_TOKEN')


def token_required(view_func):
    """Custom decorator to check for correct session token"""

    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        # Check if the token is present in session
        if 'auth_token' not in request.session:
            return redirect('/app_generic/login')  # Redirect to login if no token

        # Check if the token matches the expected token value
        if request.session['auth_token'] != EXPECTED_TOKEN:
            return redirect('/app_generic/login')  # Redirect to login if the token is incorrect

        # If token is valid, proceed with the view
        return view_func(request, *args, **kwargs)

    return _wrapped_view