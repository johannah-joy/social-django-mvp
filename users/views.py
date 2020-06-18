from django.shortcuts import render, redirect
from django.views import generic
from django.urls import reverse_lazy, reverse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout

# Create your views here.

class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    template_name = 'signup.html'
    success_url = reverse_lazy('login')


class LoginView(generic.DetailView):
    template_name = 'login.html'
    success_url = reverse_lazy('home')


def logout_view(request):
    logout(request)
    return redirect('login')