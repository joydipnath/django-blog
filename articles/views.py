from django.shortcuts import render, redirect
from .models import Article
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

