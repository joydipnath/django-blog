from django.conf.urls import url
from . import views

app_name = 'articles'

urlpatterns = [

    url(r'^$', views.article_list, name="list"),
    url(r'^create/$', views.article_create, name="create"),

    url(r'^comments/$', views.article_post_comments, name="post_comments"),
    url(r'^reply/$', views.articles_comments_reply, name="reply_comments"),
    url(r'^search/$', views.search_article, name="search_article"),


    url(r'^edit/(?P<slug>[\w-]+)/$', views.article_edit, name="edit"),
    url(r'^(?P<slug>[\w-]+)/$', views.article_detail, name="detail"), # Put it a last otherwise it will match to other routes conditions
]