from datetime import date

from django import forms
from django.core.exceptions import ValidationError

from .models import Post


class PostForm(forms.ModelForm):
    content = forms.CharField(min_length=5)

    class Meta:
        model = Post
        fields = ['title', 'content', 'categories', 'author']

    def clean(self):
        cleaned_data = super().clean()
        content = cleaned_data.get("content")
        title = cleaned_data.get("title")

        if title == content:
            raise ValidationError(
                "Описание не должно быть идентично названию."
            )

        return cleaned_data

    # def clean(self):
    #     cleaned_data = super().clean()
    #     author = cleaned_data['author']
    #     today = date.today()
    #     post_limit = Post.objects.filter(author=author, date_published__date=today).count()
    #     if post_limit >= 3:
    #         raise ValidationError("Нельзя публиковать бльше трех постов в сутки!!!")
    #     return cleaned_data
