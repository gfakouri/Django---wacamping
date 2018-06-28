from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    #return HttpResponse("HELLO")

    return render(request, 'camping/index.html')

def map(request):
    return render(request, 'camping/map.html', {})

def gallery(request):
    return render(request, 'camping/gallery.html', {})

def lingaReview(request):
    return render(request, 'camping/lingaReview.html', {})