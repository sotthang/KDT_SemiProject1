from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm, CustomUserChangeForm, CustomPasswordChangeForm, LoginForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model

# Create your views here.

def login(request):
    if request.method == 'POST':
        form = LoginForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('articles:index')
        
    else:
        form = LoginForm()
    
    context = {
        'form': form,
    }
    return render(request, 'accounts/login.html', context)


@login_required
def logout(request):
    auth_logout(request)
    return redirect('articles:index')


def signup(request):
    return render(request, 'accounts/signup.html')


def delete(request):
    return render(request, 'accounts/login.html')


def update(request):
    return render(request, 'accounts/update.html')


def change_password(request):
    return render(request, 'accounts/change_password.html')

