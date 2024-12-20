"""Module providing the views for the Generic Application"""

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.shortcuts import render, redirect

from puppybank.settings import STATIC_AUTH_TOKEN


def home(request):
    """Function-based view for Home"""
    return render(request, "app_generic/login.html")


from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.shortcuts import render, redirect


def login_view(request):
    """Function-based view for Login"""

    # Check if the session token is already set
    if 'auth_token' in request.session:
        # If the token is already set, you can redirect to a dashboard or home page
        return redirect('app_dashboard:dashboard')  # Or wherever you want to go if token exists

    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)  # User is logged in

            # Set the static token in session after login
            request.session['auth_token'] = STATIC_AUTH_TOKEN

            # Check for 'next' URL or default to 'dashboard'
            next_url = request.POST.get('next', 'app_dashboard:dashboard')
            return redirect(next_url)
    else:
        form = AuthenticationForm()

    return render(request, 'app_generic/login.html', {'form': form})


def logout_view(request):
    """Function-based view for Logout"""
    logout(request)
    return redirect('app_generic:login')


def about_outside(request):
    """Function-based view for About Page"""
    return render(request, 'app_generic/about_outside.html')


def about_inside(request):
    """Function-based view for About Page"""
    return render(request, 'app_generic/about_inside.html')
