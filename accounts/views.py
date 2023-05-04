from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.contrib.auth import update_session_auth_hash
from articles.models import Article, Plan, ArticlePlan
from .forms import CustomUserCreationForm, CustomUserChangeForm, CustomPasswordChangeForm, LoginForm
from articles.models import Article
# Create your views here.

def login(request):
    if request.user.is_authenticated:
        return redirect('accounts:index')
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
    if request.user.is_authenticated:
        auth_logout(request)
    return redirect('articles:index')


def signup(request):
    if request.user.is_authenticated:    
        return redirect('articles:index')
    
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            user.profile_img = form.cleaned_data['profile_img']
            user.save()
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
    if request.user.is_authenticated:
        request.user.delete()
        auth_logout(request)
    return redirect('articles:index')


@login_required
def update(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            user = form.save()
            user.profile_img = form.cleaned_data['profile_img']
            user.save()
            return redirect('accounts:profile', user.username)
    else:
        form = CustomUserChangeForm(instance=request.user)
    context = {
        'form': form,
    }
    return render(request, 'accounts/update.html', context)


@login_required
def change_password(request):
    if request.method == 'POST':
        form = CustomPasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            return redirect('articles:index')
    else:
        form = CustomPasswordChangeForm(user=request.user)
    context = {
        'form': form,
    }
    return render(request, 'accounts/change_password.html', context)


def profile(request, username):
    User = get_user_model()
    person = User.objects.get(username=username)
    article_count = Article.objects.filter(user=person).count()
    
    if Plan.objects.filter(user_id=request.user.id, user=person):
        plan = Plan.objects.filter(user=request.user, user_id=person.id)
        articleplans = ArticlePlan.objects.filter(plan__in=plan).select_related('article')
    else:
        articleplans = None
        plan = None
    context = {
        'person': person,
        'articleplans': articleplans,
        'article_count': article_count,
        'plan': plan,
    }
    return render(request, 'accounts/profile.html', context)


@login_required
def follow(request, user_pk):
    User = get_user_model()
    person = User.objects.get(pk=user_pk)
    if person != request.user:
        if person.followers.filter(pk=request.user.pk).exists():
            person.followers.remove(request.user)
        else:
            person.followers.add(request.user)
    return redirect('accounts:profile', person.username)

