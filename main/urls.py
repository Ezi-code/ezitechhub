from django.urls import path
from . import views

# url patterns, urls amd their names 
urlpatterns = [
    path('', views.home, name='home'),
    path('services', views.services, name='services'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact')
]