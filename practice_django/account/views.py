from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.views import LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import TemplateView, FormView, RedirectView, UpdateView
from django.urls import reverse_lazy

from .forms import UserRegistrationForm, UserAuthenticationForm, UserEditForm


class AnonymousRequiredMixin:
    redirect_url = reverse_lazy('account:profile')

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(self.redirect_url)
        return super().dispatch(request, *args, **kwargs)


class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'account/profile.html'
    login_url = 'account:sign_up'


class UserEditView(LoginRequiredMixin, UpdateView):
    template_name = 'account/user_edit.html'
    form_class = UserEditForm
    success_url = reverse_lazy('account:profile')

    def get_object(self, queryset=None):
        return self.request.user


class SignUpView(AnonymousRequiredMixin, FormView):
    template_name = 'account/sign_up.html'
    form_class = UserRegistrationForm
    success_url = reverse_lazy('account:profile')

    def form_valid(self, form):
        user = form.save(commit=False)
        login(self.request, user)
        return super().form_valid(form)


class SignInView(AnonymousRequiredMixin, FormView):
    template_name = 'account/sign_in.html'
    form_class = UserAuthenticationForm
    success_url = reverse_lazy('account:profile')

    def form_valid(self, form):
        user = form.get_user()
        if user:
            login(self.request, user)
            return super().form_valid(form)
        else:
            form.add_error(None, 'Invalid username or password')
            return super().form_invalid(form)


class CustomLogOutView(LogoutView):
    next_page = reverse_lazy('account:sign_in')
