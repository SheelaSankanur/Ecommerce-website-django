from django.shortcuts import render
import json
from shop.models import Product
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.urls import reverse
from django.contrib.auth import logout

def index(request):
    categories = Product.objects.values_list('category', flat=True).distinct()
    category_cards = []

    for category in categories:
        product = Product.objects.filter(category=category).first()
        if product:
            category_cards.append({
                'category': category,
                'image': product.image,     
                'product_id': product.product_id    
            })

    return render(request, 'index.html', {'category_cards': category_cards})


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
            return redirect("home")  # or whatever your home URL name is
        else:
            messages.error(request, "Invalid username or password")
            return render(request, "login.html", {"error": "Invalid credentials"})
            return redirect("home")
    # Handle GET request (show the login form)
    return render(request, "login.html")


def user_logout(request):
    logout(request)
    return redirect('/')