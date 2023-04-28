from django import forms
from .models import Article, Comment, Review


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ('title', 'content', 'image',)


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('title', 'content', 'image',)
