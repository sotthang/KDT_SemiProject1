from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm, CustomUserChangeForm, CustomPasswordChangeForm, LoginForm

# Create your views here.

def login(request):
    return render(request, 'accounts/login.html')


def logout(request):
    return render(request, 'accounts/login.html')


def signup(request):
    if request.user.is_authenticated:    
        return redirect('articles:main')
    
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # 회원 가입 성공 시 바로 로그인
            auth_login(request, user)
            return redirect('articles:index')
    else:
        form = CustomUserCreationForm()
    
    context = {
        'form': form,
    }

    return render(request, 'accounts/signup.html', context)


def delete(request):
    request.user.delete()
    auth_logout(request)
    return redirect('articles:index')


def update(request):
    return render(request, 'accounts/update.html')


def change_password(request):
    return render(request, 'accounts/change_password.html')

