from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
    title = forms.CharField(max_length=20)
    time = forms.CharField(max_length=20)
    place = forms.CharField(max_length=20)
    memo = forms.CharField(max_length=100)

    class Meta:
        model = Article
        # fields = ('name', 'age', 'balance', )
        fields = '__all__'
