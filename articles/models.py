from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Article(models.Model):

    title = models.CharField(max_length=100)
    slug = models.SlugField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    thumb = models.ImageField(default='default.png', blank=True)
    key_words = models.CharField(max_length=100)
    author = models.ForeignKey(User, default=None, on_delete=models.CASCADE, related_name='user')
    up_vote = models.PositiveSmallIntegerField(null=True)
    # add in thumbnail

    def __str__(self):
        return self.title

    def snippet(self):
        return self.body[:50]+"..."



class Comment(models.Model):

    comment = models.CharField(max_length=200)
    author  = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, default=None, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add = True)
    up_vote = models.PositiveSmallIntegerField(null=True)
    down_vote = models.PositiveSmallIntegerField(null=True)

    def __str__(self):
        return self.comment



class ReplyOnComment(models.Model):

    reply = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add = True)
    author  = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, default=None, on_delete=models.CASCADE)
    up_vote = models.PositiveSmallIntegerField(null=True)
    down_vote = models.PositiveSmallIntegerField(null=True)

    def __str__(self):
        return self.reply