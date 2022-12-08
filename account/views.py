from django.contrib.auth.mixins import AccessMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import View, UpdateView, TemplateView, FormView
from .forms import SignUpForm, UserLoginForm
from django.contrib.auth.models import User

from django.contrib import messages
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .token import account_activation_token

from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from django.utils.encoding import force_str


class LoginRequired(AccessMixin):
    """Verify that the current user is authenticated."""

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect("account:login")
        return super().dispatch(request, *args, **kwargs)


class SignUpView(View):
    form_class = SignUpForm
    template_name = "account/login.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect("account:login")
        return render(request, self.template_name, {'form': form})


class LoginView(FormView):
    """
        Used to manage User Login view
    """
    form_class = UserLoginForm
    template_name = "account/login.html"

    def form_valid(self, form):
        user = form.cleaned_data
        user.backend = 'django.contrib.auth.backends.ModelBackend'
        login(self.request, user)
        return redirect("core:home")

    def form_invalid(self, form):
        return super().form_invalid(form)


class LogoutView(FormView):
    """
        Used to manage User Logout View
    """

    def get(self, *args, **kwargs):
        logout(self.request)
        messages.success(self.request, "User logged out successfully.")
        return redirect("account:login")
