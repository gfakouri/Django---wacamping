#from django.urls import path
from . import views


from django.urls import path

urlpatterns = [
    path('', views.blogIndex, name='blogIndex'),
    path('details/<int:id>/', views.details, name='details'),
    #path('map/', views.map, name = 'map'),
    #path('gallery/', views.gallery, name = 'gallery')
]