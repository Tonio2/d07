from django import forms
from .models import Article, UserFavouriteArticle


class CreateArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ["title", "synopsis", "content"]
        labels = {"title": "Title", "synopsis": "Synopsis", "content": "Content"}
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "synopsis": forms.TextInput(attrs={"class": "form-control"}),
            "content": forms.Textarea(attrs={"class": "form-control"}),
        }

class UserFavouriteArticleForm(forms.ModelForm):
    class Meta:
        model = UserFavouriteArticle
        fields = []
