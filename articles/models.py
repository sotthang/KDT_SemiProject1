from django.db import models
from django.conf import settings
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class Article(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    category = models.CharField(max_length=50, default='체험관광')
    content = models.CharField(max_length=1000)
    image = ProcessedImageField(upload_to='', processors=[ResizeToFill(500, 250)], format='JPEG',options={'quality': 100})
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    emote_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='emote_articles', through='Emote')
    lat = models.DecimalField(max_digits=10, decimal_places=7)
    lng = models.DecimalField(max_digits=10, decimal_places=7)


class Review(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    content = models.CharField(max_length=1000)
    image = ProcessedImageField(blank=True, upload_to='', processors=[ResizeToFill(500, 250)], format='JPEG',options={'quality': 100})
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    emote_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='emote_reviews', through='Emote')
    score = models.PositiveIntegerField(default=3, validators=[MinValueValidator(0), MaxValueValidator(5)])


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.CharField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class ReviewComment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    review = models.ForeignKey(Review, on_delete=models.CASCADE)
    content = models.CharField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Emote(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    emotion = models.CharField(max_length=50)
    article = models.ForeignKey(Article, null=True, on_delete=models.CASCADE)
    review = models.ForeignKey(Review, null=True, on_delete=models.CASCADE)
