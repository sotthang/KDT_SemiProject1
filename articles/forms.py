from django import forms
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
            'title': forms.TextInput(attrs={'class':'form-control',}),
            'category': forms.TextInput(attrs={'class':'form-control',}),
            'content': forms.Textarea(attrs={'class':'form-control', 'rows':'5',}),

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
        
        
class ReviewForm(forms.ModelForm):
    class Meta:
        
        model = Review
        exclude = ('user', 'emote_users', 'article')
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
        

