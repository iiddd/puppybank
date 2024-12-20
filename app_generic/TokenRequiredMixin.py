from django.shortcuts import redirect
from django.conf import settings

EXPECTED_TOKEN = getattr(settings, 'STATIC_AUTH_TOKEN')

class TokenRequiredMixin:
    """Mixin to enforce session token validation"""
    def dispatch(self, request, *args, **kwargs):
        # Check if the token exists and is valid
        if 'auth_token' not in request.session or request.session['auth_token'] != EXPECTED_TOKEN:
            return redirect('/bank/login')  # Redirect to login if token is missing or invalid
        return super().dispatch(request, *args, **kwargs)