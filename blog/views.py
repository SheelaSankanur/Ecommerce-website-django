from django.shortcuts import render
from .models import BlogPost
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login
# from django.urls import reverse
from django.contrib.auth import logout

def index(request):
    blogposts = BlogPost.objects.all()
    return render(request, 'blog/index.html', {'blogposts': blogposts})

def blogpost(request, id):
    blogpost = BlogPost.objects.filter(post_id=id)[0]
    return render(request, 'blog/blogpost.html' , {'blogpost': blogpost})

def blogposts(request):
    blogposts = BlogPost.objects.all()
    return render(request, 'blog/blogpost.html', {'blogposts': blogposts})


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        if User.objects.filter(username=username).exists():
            messages.error(request, "User already exists")
            return redirect('register')

        user = User.objects.create_user(username=username, password=password)
        user.save()
        return redirect('login')

    return render(request, 'register.html')

def user_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            return render(request, "login.html", {"error": "Invalid credentials"})

    return render(request, "login.html")

def user_logout(request):
    logout(request)
    return redirect('/')