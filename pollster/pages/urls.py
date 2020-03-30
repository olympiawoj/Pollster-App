from django.urls import path 

from . import views 


#create a route and bring into main urls.py
urlpatterns = [
    path('', views.index, name='index'),
]