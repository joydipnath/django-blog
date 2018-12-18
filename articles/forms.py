from django import forms
from . import models


class CreateArticle(forms.ModelForm):
    class Meta:
        model = models.Article
        fields = [ 'title', 'body', 'slug', 'thumb', 'key_words', 'visibility', 'allow_comments' ]

class PostComment(forms.ModelForm):
	class Meta:
		model = models.Comment
		fields = [ 'comment' ]