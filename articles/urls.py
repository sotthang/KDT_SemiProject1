from django.urls import path
from . import views


app_name = 'articles'
urlpatterns = [
    path('', views.index, name='index'),
    path('articles/create/', views.create, name='create'),
    path('articles/<int:article_pk>/', views.detail, name='detail'),
    path('articles/<int:article_pk>/delete/', views.delete, name='delete'),
    path('articles/<int:article_pk>/update/', views.update, name='update'),
    path('articles/<int:article_pk>/comments/', views.comment_create, name='comment_create'),
    path('articles/<int:article_pk>/comments/<int:comment_pk>/delete/', views.comment_delete, name='comment_delete'),
    path('articles/<int:article_pk>/comments/<int:comment_pk>/update/', views.comment_update, name='comment_update'),
    path('articles/<int:article_pk>/reviews/create/', views.review_create, name='review_create'),
    path('reviews/<int:review_pk>/', views.review_detail, name='review_detail'),
    path('reviews/<int:review_pk>/comments/', views.review_comment_create, name='review_comment_create'),
    path('reviews/<int:review_pk>/comments/<int:comment_pk>/delete', views.review_comment_delete, name='review_comment_delete'),
    path('reviews/<int:review_pk>/comments/<int:comment_pk>/update', views.review_comment_update, name='review_comment_update'),
]
