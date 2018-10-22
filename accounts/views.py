from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.http import HttpResponse

# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import logout, login
from django.http import HttpResponseRedirect
from django.db import transaction
from .models import Profile
from .forms import UserForm,ProfileForm
from articles.models import Article

# get signup/registration form 
def signup_view(request):

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # login(request, user)
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return redirect('articles:list')
    else:
        form = UserCreationForm()

    return render(request, 'accounts/signup.html', { 'form': form })

# Get the login view
def login_view(request):

    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('articles:list')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', { 'form': form })

# Logout the user from app
def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('articles:list')


# Show dashboard
@login_required(login_url="/accounts/login/")
def dashboard(request):
    user_id = request.user.id

    user_form = UserForm(instance=request.user)
    # return HttpResponse(user_id)
    # articles = Article.objects.all().order_by('date') 
    # articles =  Article.objects.get(author=user_id)

    articles = Article.objects.filter(author=user_id).values()

    # return HttpResponse(articles)

    return render(request, 'accounts/dashboard.html', { 'articles': articles, 'user_form': user_form })


@login_required
@transaction.atomic
def update_profile(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return HttpResponseRedirect('/')
        else:
            return HttpResponseRedirect('/')
            # messages.error(request, ('Please correct the error below.'))
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
    return render(request, 'accounts/dashboard.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })