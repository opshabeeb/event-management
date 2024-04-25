from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('about',views.about,name='about'),
    path('booking',views.booking,name='booking'),
    path('contact',views.contact,name='contact'),
    path('Services',views.event,name='event'),
    path("edit/<int:id>",views.editevent,name='edit'),
    path("<int:id>/formupdate",views.formupdate,name='formupdate'),
]