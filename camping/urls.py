#from django.urls import path
from . import views


from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('map/', views.map, name = 'map'),
    path('gallery/', views.gallery, name = 'gallery'),
    path('lingaReview/', views.lingaReview, name = 'lingaReview')
]