from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Article, Comment, Review
from .forms import ArticleForm, CommentForm, ReviewForm, ReviewCommentForm

# Create your views here.

def index(request):
    articles = Article.objects.all()
    
    context = {
        'articles': articles,
    }

    return render(request, 'articles/index.html', context)


def detail(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    reviews = Review.objects.filter(article=article_pk)
    comments = article.comment_set.all()
    comment_form = CommentForm()
    form = CommentForm(request.POST, instance=article)
    context = {
        'article': article,
        'comments': comments,
        'comment_form': comment_form,
        'form': form,
        'reviews': reviews,
    }
    return render(request, 'articles/detail.html', context)


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
    context = {
        'article': article,
        'form': form,
    }
    return render(request, 'articles/update.html', context)


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


def review_detail(request, article_pk, review_pk):
    review = Review.objects.get(pk=review_pk)
    comments = review.comment_set.all()
    reviewcomment_form = ReviewCommentForm()
    form = ReviewCommentForm(request.POST, instance=review)
    context = {
        'review': review,
        'comments': comments,
        'reviewcomment_form': reviewcomment_form,
        'form': form,
    }
    return render(request, 'reviews/review_detail.html', context)


@login_required
def review_create(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    if request.method == 'POST':
        form = ReviewForm(request.POST, request.FILES)
        if form.is_valid():
            review = form.save(commit=False)
            review.article = article
            review.user = request.user
            review.save()
            return redirect('articles:review_detail', article.pk, review.pk)
    else:
        form = ReviewForm()
    
    context = {
        'form': form,
        'article': article,
    }

    return render(request, 'reviews/review_create.html', context)


@login_required
def review_delete(request, article_pk, review_pk):
    review = Review.objects.get(pk=review_pk)
    
    if review.user == request.user:
        review.delete()
    
    return redirect('articles:detail', article_pk)


@login_required
def review_update(request, article_pk, review_pk):
    review = Review.objects.get(pk=review_pk)
    if request.user == review.user:
        if request.method == 'POST':
            form = ReviewForm(request.POST, request.FILES, instance=review)
            if form.is_valid():
                form.save()
                return redirect('articles:detail', article_pk)
        else:
            form = ReviewForm(instance=review)
    else:
        return redirect('articles:detail', article_pk)
    context = {
        'review': review,
        'form': form,
    }
    return render(request, 'articles/review/review_update.html', context)
