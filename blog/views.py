from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader, context

def about(request):
    # template = loader.get_template('blog/about.html')
    #return HttpResponse(template.render())
    context = ""
    return render(request, 'blog/about.html')
    # return render(request, template)

def homepage(request):
    # return HttpResponse("homepage")
    return render(request, 'home.html')