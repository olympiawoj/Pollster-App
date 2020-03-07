from django.urls import path 

from . import views 


app_name = 'polls'

#create a route and bring into main urls.py
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>', views.detail, name="detail"),
]