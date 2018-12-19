from django import forms
from . import models


# class CreateArticle(forms.ModelForm):
#     class Meta:
#         model = models.Article
#         fields = [ 'title', 'body', 'slug', 'thumb', 'key_words', 'visibility', 'allow_comments' ]


class CreateArticle(forms.ModelForm):
    # ...
    class Meta:
        model = models.Article
        fields = [ 'title', 'body', 'slug', 'thumb', 'key_words', 'visibility', 'allow_comments' ]

    def clean(self):
        cleaned_data = self.cleaned_data
        title = cleaned_data.get("title")
        body = cleaned_data.get("body")
        slug = cleaned_data.get("slug")
        key_words = cleaned_data.get("key_words")
        visibility = cleaned_data.get("visibility")
        allow_comments = cleaned_data.get("allow_comments")

        # if end_date and start_date:
        #     if end_date < start_date:
        #         msg = 'Event end date should not occur before start date.'
        #         self._errors['end_date'] = self.error_class([msg])
        #         del cleaned_data['end_date']

        # form.add_error('field_name', 'error_msg or ValidationError instance') If the field_name is None the error will be added to non_field_errors.
        
        # if end_date and start_date:
        # if end_date < start_date:
        #     self.add_error('end_date', 'Event end date should not occur before start date.')
            # You can use ValidationError as well
            # self.add_error('end_date', form.ValidationError('Event end date should not occur before start date.'))


        return cleaned_data


# class ArticleForm(forms.Form):

#     # Everything as before.
#     def clean(self):
#         cleaned_data = super(ArticleForm, self).clean()
#         title = cleaned_data.get("title")
#         body = cleaned_data.get("body")
#         slug = cleaned_data.get("slug")
#         key_words = cleaned_data.get("key_words")
#         visibility = cleaned_data.get("visibility")
#         allow_comments = cleaned_data.get("allow_comments")


class PostComment(forms.ModelForm):
	class Meta:
		model = models.Comment
		fields = [ 'comment' ]