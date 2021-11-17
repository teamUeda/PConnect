from django.contrib.auth import login, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import (LoginView, LogoutView)
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView

from .forms import LoginForm, UserCreateForm


class Login(LoginView):
    form_class = LoginForm
    template_name = 'login.html'


class Create_account(CreateView):
    form_class = UserCreateForm
    template_name = 'create.html'
    success_url = '../'

    def form_valid(self, form):
        if self.request.POST['next'] == '確認':
            return render(self.request, 'create-confirm.html', {'form': form})
        elif self.request.POST['next'] == '修正':
            return render(self.request, 'create.html', {'form': form})
        elif self.request.POST['next'] == '作成':
            form.save()
            user = authenticate(
                username=form.cleaned_data['user_id'],
                password=form.cleaned_data['password1'],
            )
            login(self.request, user)
            return super().form_valid(form)
        else:
            return redirect(Login)


class Top(LoginRequiredMixin, TemplateView):
    template_name = "top.html"


class Logout(LoginRequiredMixin, LogoutView):
    template_name = 'logout.html'

