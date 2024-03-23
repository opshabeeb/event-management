from django.contrib import admin
from django.urls import path,include
from user import views

urlpatterns = [
    path('login',views.loginn,name='login'),
    path('signup',views.signup,name='signup'),
    path('logout',views.logoutt,name='logout'),
]