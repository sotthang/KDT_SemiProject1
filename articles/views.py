from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    return render(request, 'articles/index.html')


def detail(request, article_pk):
    return render(request, 'articles/detail.html')


@login_required
def create(request):
    return render(request, 'articles/create.html')


@login_required
def delete(request, article_pk):
    return redirect('articles:index')


@login_required
def update(request, article_pk):
    return render(request, 'articles/update.html')


@login_required
def comment_create(request, article_pk):
    return redirect('articles:detail')


@login_required
def comment_delete(request, article_pk, comment_pk):
    return redirect('articles:detail', article_pk)


@login_required
def comment_update(request, article_pk, comment_pk):
    return render(request, 'update.html')

