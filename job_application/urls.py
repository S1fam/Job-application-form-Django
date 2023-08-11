from django.urls import path
from . import views  # views.py as module (. because they in same directory)

urlpatterns = [  # django looks for this exact variable name
    path('', views.index, name='index'),  # '' for homepage, that should be connected to views.index
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact')
]
