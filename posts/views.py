from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    #return HttpResponse("HELLO")

    return render(request, 'posts/index.html')

def map(request):
    return render(request, 'posts/map.html', {})

def gallery(request):
    return render(request, 'posts/gallery.html', {})