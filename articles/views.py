from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.http import JsonResponse
from django.db.models import Q
from django.core.paginator import Paginator
from .models import Article, Comment, Review, ReviewComment, Emote, Plan, ArticlePlan
from .forms import ArticleForm, CommentForm, ReviewForm, ReviewCommentForm, PlanForm, ArticlePlanForm
import json
from geopy.geocoders import Nominatim


# Create your views here.

def index(request):
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)


EMOTIONS = [
    {'label': '좋아요', 'value': 1},
    {'label': '재밌어요', 'value': 2},
    {'label': '그냥그래요', 'value': 3},
]


def detail(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    geolocoder = Nominatim(user_agent = 'South Korea', timeout=None)
    address = geolocoder.reverse((article.lat, article.lng))
    reviews = Review.objects.filter(article=article_pk)
    review_count = reviews.count()
    comments = article.comment_set.all()
    comment_count = comments.count()
    comment_form = CommentForm()
    form = CommentForm(request.POST, instance=article)
    emotions = []
    for emotion in EMOTIONS:
        label = emotion['label']
        value = emotion['value']
        count = Emote.objects.filter(article=article, emotion=value).count()
        if request.user.is_authenticated:
            exist = Emote.objects.filter(article=article, emotion=value, user=request.user)
        else:
            exist = False
        emotions.append(
            {
                'label': label,
                'value': value,
                'count': count,
                'exist': exist,
            }
        )
    context = {
        'article': article,
        'comments': comments,
        'comment_form': comment_form,
        'form': form,
        'reviews': reviews,
        'review_count': review_count,
        'comment_count': comment_count,
        'emotions': emotions,
        'address' : address,
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


def review_detail(request, review_pk):
    review = Review.objects.get(pk=review_pk)
    article = Article.objects.get(pk=review.article_id)
    User = get_user_model()
    person = User.objects.get(username=request.user)
    comments = review.reviewcomment_set.all()
    comment_form = ReviewCommentForm()
    comment_count = comments.count()
    emotions = []
    for emotion in EMOTIONS:
        label = emotion['label']
        value = emotion['value']
        count = Emote.objects.filter(review=review, emotion=value).count()
        if request.user.is_authenticated:
            exist = Emote.objects.filter(review=review, emotion=value, user=request.user)
        else:
            exist = False
        emotions.append(
            {
                'label': label,
                'value': value,
                'count': count,
                'exist': exist,
            }
        )
    context = {
        'person': person,
        'review': review,
        'article': article,
        'comments': comments,
        'comment_form': comment_form,
        'emotions': emotions,
        'comment_count': comment_count,
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
            return redirect('articles:review_detail', review.pk)
    else:
        form = ReviewForm()
    
    context = {
        'form': form,
        'article': article,
    }

    return render(request, 'reviews/review_create.html', context)
    
@login_required
def review_delete(request, review_pk):    
    review = Review.objects.get(pk=review_pk)
    article_pk = review.article.pk
    if review.user == request.user:
        review.delete()
    
    return redirect('articles:detail', article_pk)


@login_required
def review_update(request, review_pk):
    review = Review.objects.get(pk=review_pk)
    article_pk = review.article.pk

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
    return render(request, 'reviews/review_update.html', context)


@login_required
def review_comment_create(request, review_pk):
    review = Review.objects.get(pk=review_pk)
    form = ReviewCommentForm(request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.review = review
        comment.user = request.user
        comment.save()
        return redirect('articles:review_detail', review.pk)
    
@login_required
def review_comment_delete(request, review_pk, comment_pk):
    comment = ReviewComment.objects.get(pk=comment_pk)
    
    if request.user == comment.user:
        comment.delete()
        
    return redirect('articles:review_detail', review_pk)

@login_required
def review_comment_update(request, review_pk, comment_pk):
    comment = ReviewComment.objects.get(pk=comment_pk)
    if request.user == comment.user:
        if request.method == 'POST':
            r = list(request.POST.keys())
            js = json.loads(r[0])
            comment.content = js['content']
            comment.save()
            
    context = {
        'content': comment.content,
    }

    return JsonResponse(context)


def category_name(request, category_name):
    articles = Article.objects.filter(category=category_name)

    page = request.GET.get('page', '1')
    per_page = 5
    paginator = Paginator(articles, per_page)
    page_obj = paginator.get_page(page)
    num_page = paginator.num_pages

    context = {
        'articles': page_obj,
        'category_name': category_name,
        'num_page': num_page,
    }
    
    return render(request, 'articles/category_name.html', context)


@login_required
def emotes(request, pk, emotion, page):
    if 'Article' in page:
        article = Article.objects.get(pk=pk)
        filter_query = Emote.objects.filter(article=article, user=request.user, emotion=emotion)
        if filter_query.exists():
            filter_query.delete()
        else:
            Emote.objects.create(article=article, user=request.user, emotion=emotion)
        context = {
            'emotion_count': Emote.objects.filter(article=article, emotion=emotion).count()
        }
        return JsonResponse(context)
    elif 'Review' in page:
        review = Review.objects.get(pk=pk)
        filter_query = Emote.objects.filter(review=review, user=request.user, emotion=emotion)
        if filter_query.exists():
            filter_query.delete()
        else:
            Emote.objects.create(review=review, user=request.user, emotion=emotion)
        context = {
            'emotion_count': Emote.objects.filter(review=review, emotion=emotion).count()
        }
        return JsonResponse(context)

def search(request):
    search_word = request.GET.get('word', False)
    result_article = Article.objects.filter(Q(title__icontains=search_word) | Q(content__icontains=search_word)).order_by('-pk').distinct()[0:5]
    result_review = Review.objects.filter(Q(title__icontains=search_word) | Q(content__icontains=search_word)).order_by('-pk').distinct()[0:5]

    context = {
        'results_article': result_article,
        'results_review': result_review,
        'search_word': search_word,
    }
    return render(request, 'search/search.html', context)

def search_detail(request, category):
    search_word = request.GET.get('word')

    if category == 'article':
        results = Article.objects.filter(Q(title__icontains=search_word) | Q(content__icontains=search_word)).order_by('-pk').distinct()
        cat = 'Article'
    elif category == 'review':
        results = Review.objects.filter(Q(title__icontains=search_word) | Q(content__icontains=search_word)).order_by('-pk').distinct()
        cat = 'Review'
    
    page = request.GET.get('page', '1')
    per_page = 5
    paginator = Paginator(results, per_page)
    page_obj = paginator.get_page(page)
    num_page = paginator.num_pages
    
    context = {
        'results': page_obj,
        'category': cat,
        'num_page': num_page,
        'search_word': search_word,
    }
    return render(request, 'search/search_detail.html', context)


@login_required
def plan(request):
    articles = Article.objects.all()
    if request.method == 'POST':
        planform = PlanForm(request.POST)
        articleplanform = ArticlePlanForm(request.POST)
        if planform.is_valid():
            plan = planform.save(commit=False)
            plan.user = request.user
            plan.save()
            articleplan = articleplanform.save(commit=False)
            articleplan.plan = plan
            destinations = request.POST.getlist('destination')
            for destination in destinations:
                if 'Day' not in destination:
                    pass
                else:
                    destination_day, destination_article = destination.split('_')
                    destination_day = destination_day[-1]
                    destination_article = Article.objects.get(id=destination_article)
                    ArticlePlan.objects.create(plan=plan, day=destination_day, article=destination_article)
                    
            return redirect('accounts:profile', request.user)
    else:
        planform = PlanForm()
        articleplanform = ArticlePlanForm()
    context = {
        'articles': articles,
        'planform': planform,
        'articleplanform': articleplanform,
    }
    return render(request, 'articles/plan.html', context)


@login_required
def plan_delete(request, plan_pk):
    plan = Plan.objects.get(pk=plan_pk)
    
    if plan.user == request.user:
        plan.delete()
    
    return redirect('articles:index')

