from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['headline', 'content', 'image_filename', 'video_filename']
