from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm, CustomUserChangeForm, CustomPasswordChangeForm, LoginForm

# Create your views here.

def login(request):
    return render(request, 'accounts/login.html')


def logout(request):
    return render(request, 'accounts/login.html')


def signup(request):
    return render(request, 'accounts/signup.html')


def delete(request):
    return render(request, 'accounts/login.html')


def update(request):
    return render(request, 'accounts/update.html')


def change_password(request):
    return render(request, 'accounts/change_password.html')

