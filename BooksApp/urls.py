from django.contrib import admin
from django.urls import path
from django.urls import path
from . import views


#Url patterns for the pages we have
urlpatterns = [
    path('', views.Books, name='home-page'),
    path('AddBooks', views.AddBooks, name='add-page'),
    path('snippet', views.snippet_detail)
]
