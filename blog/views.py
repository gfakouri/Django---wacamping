from django.shortcuts import render
from django.http import HttpResponse

from .models import Blog

# Create your views here.

def blogIndex(request):
    #return HttpResponse("HELLO")

    blog = Blog.objects.all()[:10]

    context = {
        'title' : 'latest post',
        'blog' : blog
    }

    return render(request, 'blog/blogIndex.html', context)

def details(request, id):
    blog = Blog.objects.get(id=id)

    context = {
        'blog' : blog
    }

    return render(request, 'blog/details.html', context)
