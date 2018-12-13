from django.shortcuts import render, redirect
from .models import Article, Comment, ReplyOnComment
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from . import forms
from django.db.models import Q

# Create your views here.


def article_list(request):
    articles = Article.objects.all().order_by('date')
    return render(request, 'articles/article_list.html', {'articles': articles})


def article_detail(request, slug):
    
    article = Article.objects.get(slug=slug)
    # [:1]
    # return article.author_set.all()
    # return HttpResponse(article.author_set.all())
    return render(request, 'articles/article_detail.html', {'article': article})


@login_required(login_url="/accounts/login/")
def article_create(request):
    if request.method == 'POST':
        form = forms.CreateArticle(request.POST, request.FILES)
        if form.is_valid():
            # save to data db
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect('articles:list')
    else:
        form = forms.CreateArticle()
    return render(request, 'articles/article_create.html', {'form': form})

def search_article(request):
    try:
        q = request.GET['search']
        # article = Article.objects.all().order_by('date')
        # article = Article.objects.filter(Q(title__search=q)) #| Q(slug__search=q) | Q(body__search=q))
        article = Article.objects.filter(title__icontains=q)
        # return article

        return render(request, 'articles/article_list.html', {'articles' : article, 'search': q })
    except KeyError:
        return render(request, 'articles/article_list.html')


@login_required(login_url="/accounts/login")
def article_post_comments(request):

   
    if request.method == 'POST':
        # form = forms.PostComment(request.POST)
        comments = request.POST.get("comment") 
        author_id = request.user.id
        article_id = request.POST.get("article_id")
        b = Comment.objects.create(comment=request.POST.get("comment"), article_id=request.POST.get("article_id"), author_id = request.user.id)
        # b = Comment.objects.create(comment=comments, article_id = article_id, author_id = author_id)
        b.save()
        # if form.is_valid():
        #     # save to data db
        #     instance = form.save(commit=False)
        #     instance.author = request.user
        #     instance.article = request.POST.get("article_id")
        #     instance.save()
        #     # return HttpResponse(request.POST.get("article_id"))
        #     return redirect('articles:list')
    # else:
    #     form = forms.CreateArticle()
    article = Article.objects.get(id=request.POST.get("article_id"))
    # return redirect('articles:detail', {'article': article})
    return render(request, 'articles/article_detail.html', {'article': article})



def articles_comments_reply(request):
    return HttpResponse("hi")