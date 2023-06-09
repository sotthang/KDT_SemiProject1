from django.urls import path
from . import views


app_name = 'articles'
urlpatterns = [
    path('', views.index, name='index'),
    path('articles/create/', views.create, name='create'),
    path('articles/<int:article_pk>/', views.detail, name='detail'),
    path('articles/<str:category_name>/', views.category_name, name='category_name'),
    path('articles/<int:article_pk>/delete/', views.delete, name='delete'),
    path('articles/<int:article_pk>/update/', views.update, name='update'),
    path('articles/<int:article_pk>/comments/', views.comment_create, name='comment_create'),
    path('articles/<int:article_pk>/comments/<int:comment_pk>/delete/', views.comment_delete, name='comment_delete'),
    path('articles/<int:article_pk>/comments/<int:comment_pk>/update/', views.comment_update, name='comment_update'),
    path('articles/<int:article_pk>/reviews/create/', views.review_create, name='review_create'),
    path('reviews/<int:review_pk>/', views.review_detail, name='review_detail'),
    path('reviews/<int:review_pk>/delete/', views.review_delete, name='review_delete'),
    path('reviews/<int:review_pk>/update/', views.review_update, name='review_update'),
    path('reviews/<int:review_pk>/comments/', views.review_comment_create, name='review_comment_create'),
    path('reviews/<int:review_pk>/comments/<int:comment_pk>/delete/', views.review_comment_delete, name='review_comment_delete'),
    path('reviews/<int:review_pk>/comments/<int:comment_pk>/update/', views.review_comment_update, name='review_comment_update'),
    path('articles/<int:pk>/emotes/<int:emotion>/<str:page>/', views.emotes, name='emotes'),
    path('search/', views.search, name='search'),
    path('search/<str:category>/', views.search_detail, name='search_detail'),
    path('plan/', views.plan, name='plan'),
    path('plan/<int:plan_pk>/delete/', views.plan_delete, name='plan_delete'),
]
