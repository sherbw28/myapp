from django import forms
from .models import Article

class SearchForm(forms.Form):
    keyword = forms.CharField(label="検索", max_length=100)
    
class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ('content', 'name')
        
        widgets = {
            'content': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'content'}),
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'write your name'}),
        }