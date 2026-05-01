from turtle import home
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='BlogHome'),
    path('blogpost/<int:id>', views.blogpost, name='BlogPost'),
    path('blogpost/', views.blogposts, name='BlogPost'),
    path("", home, name="home"),   
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    
]