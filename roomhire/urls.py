from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('book/', views.book, name='book'),
    path('bookingrequestsuccessful/', views.success, name='success'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('allevents/', views.all_events, name='event-request'),
    path('confirmedevents/', views.confirm_e, name='confirm'),
    path('calendar/', views.calendar, name='calendar'),
    path('upcomingevents/', views.upcomingevents, name='upcomingevents'),
    path('info/', views.info, name='info'),
    path('clubinfo/', views.clubinfo, name='clubinfo'),
    path('bespoke-events/', views.balloons, name='baloon'),
    path('lbd/', views.lbd, name='food'),
    path('manage-users/', views.manageusers, name='manage-users'),
    path('admin/auth/user/', views.goadmin, name='admin'),
    
]
