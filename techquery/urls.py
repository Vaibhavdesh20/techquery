from django.contrib import admin
from django.urls import path,include
from techquery import views

urlpatterns = [
    
    path('',views.index,name='index'),
    path('signup',views.signup,name='signup'),
    path('signup',views.signup,name='signup'),
    path('about',views.about,name='about'),
    path('login',views.login,name='login'),
    path('info',views.info,name='info'),
    path('contact',views.contact,name='contact.html'),
    
]
