from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Article, Comment
from .forms import ArticleForm, CommentForm

# Create your views here.

def index(request):
    return render(request, 'articles/index.html')


def detail(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    context = {
        'article': article,
    }
    return render(request, 'articles/detail.html', context)


@login_required
def create(request):
    return render(request, 'articles/create.html')


@login_required
def delete(request, article_pk):
    return redirect('articles:index')


@login_required
def update(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    if request.user == article.user:
        if request.method == 'POST':
            form = ArticleForm(request.POST, request.FILES, instance=article)
            if form.is_valid():
                form.save()
                return redirect('articles:detail', article.pk)
        else:
            form = ArticleForm(instance=article)
            
    else:
        return redirect('articles:index')


@login_required
def comment_create(request, article_pk):
    if request.method == "POST":
        article = Article.objects.get(pk=article_pk)
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.article = article
            comment.user = request.user
            comment.save()
        return redirect('articles:detail', article.pk)


@login_required
def comment_delete(request, article_pk, comment_pk):
    if request.method == "POST":
        comment = Comment.objects.get(pk=comment_pk)
        if request.user == comment.user:
            comment.delete()
    return redirect('articles:detail', article_pk)


@login_required
def comment_update(request, article_pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    article = Article.objects.get(pk=article_pk)
    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            return redirect('articles:detail', article.pk)
    else:
        form = CommentForm(instance=comment)
    context = {
        'comment': comment,
        'form': form,
    }
    return render(request, 'update.html', context)

