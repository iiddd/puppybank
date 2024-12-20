from django.utils.deprecation import MiddlewareMixin

from puppybank.settings import STATIC_AUTH_TOKEN


def process_request(request):
    # Check if token is already set in session
    if 'auth_token' not in request.session:
        # Set a static token if not present
        request.session['auth_token'] = STATIC_AUTH_TOKEN

    # Optionally log or debug the token
    # print(f"Token set in session: {request.session['auth_token']}")

    return None


class SetAuthTokenMiddleware(MiddlewareMixin):
    pass
