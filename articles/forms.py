from django import forms
from django.forms import ClearableFileInput
from .models import Article, Comment, Review, ReviewComment, Emote



class ArticleForm(forms.ModelForm):
    CATEGORY_CHOICES = [
        ('숙소','숙소'),
        ('자연명소','자연명소'),
        ('테마파크','테마파크'),
        ('체험관광','체험관광'),
        ('레저 & 액티비티','레저 & 액티비티'),
        ('맛집','맛집'),
        ('쇼핑','쇼핑'),
    ]
    category = forms.ChoiceField(
        label = '카테고리',
        widget = forms.Select(
            attrs = {
                'class': 'my-category form-control',
                'style': 'border:none;'
            }
        ),
        choices = CATEGORY_CHOICES,
    )
    class Meta:
        model = Article
        exclude = ('user', 'emote_users')
        labels = {
            'title': '제목',
            'content': '내용',
            'image': '이미지',
        }
        widgets = {
            'title': forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder' : '제목을 입력해 주세요',
                    'style': 'border:none;',
                }
            ),
            'content': forms.Textarea(
                attrs={
                    'class':'form-control',
                    'placeholder' : '내용을 입력해 주세요',
                    'rows':'5',
                    'style': 'border:none;'
                }
            ),
            'image': ClearableFileInput(
                attrs={
                    'class': 'form-control',
                    'style': 'width: 400px;'
                }
            ),
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)
        labels = {
            'content': '댓글',
        }
        widgets = {
            'content': forms.Textarea(attrs={'class':'form-control', 'rows':'2',})
        }
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.errors:
            for f_name in self.fields:
                if f_name in self.errors:
                    self.fields[f_name].widget.attrs.update({'aria-describedby': f"{f_name}_invalid"})
                    self.fields[f_name].widget.attrs.update({'aria-invalid': 'true'})
                    self.errors.pop(f_name)
                else:
                    self.fields[f_name].widget.attrs.update({'class': 'form-control'})
                    self.fields[f_name].widget.attrs.update({'aria-describedby': f"{f_name}_help"})
                    self.fields[f_name].widget.attrs.update({'aria-invalid': 'false'})


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        exclude = ('user', 'emote_users', 'article',)
        labels = {
                'title': '제목',
                'content': '내용',
                'image': '이미지',    
                'score': '별점',
            }
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control',}),
            'content': forms.Textarea(attrs={'class':'form-control', 'rows':'5',}),
            'score': forms.NumberInput(attrs={'class':'form-control',}),
        }


class ReviewCommentForm(forms.ModelForm):
    class Meta:
        model = ReviewComment
        fields = ('content',)
        labels = {
            'content': '댓글',
        }
        widgets = {
            'content': forms.Textarea(attrs={'class':'form-control', 'rows':'2',})
        }
        
class EmoteForm(forms.ModelForm):
    class Meta:
        model = Emote
        fields = ('emotion',)
        

