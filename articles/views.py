from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Article, Comment
from .forms import ArticleForm, CommentForm
# Create your views here.

def index(request):
    articles = Article.objects.all()
    
    context = {
        'articles': articles,
    }

    return render(request, 'articles/index.html', context)


def detail(request, article_pk):
    return render(request, 'articles/detail.html')


@login_required
def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save(commit=False)
            article.user = request.user
            article.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm()
    
    context = {
        'form': form,
    }

    return render(request, 'articles/create.html', context)


@login_required
def delete(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    
    if article.user == request.user:
        article.delete()
    
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

