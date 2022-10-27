from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('book/', views.book, name='book'),
    path('bookingrequestsuccessful/', views.success, name='success'),
]
