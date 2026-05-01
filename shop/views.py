from django.shortcuts import render
from django.http import HttpResponse
from .models import Product, Contact, Order, Orderupdate
from math import ceil
import json

def index(request):
    from math import ceil
    all_products = []
    category_cards = []
    categories = Product.objects.values_list('category', flat=True).distinct()

    for index, category in enumerate(categories):
        products = Product.objects.filter(category=category)
        n = len(products)
        nslides = n // 4 + ceil((n / 4) - (n // 4))
        all_products.append({
            'products': products,
            'range': range(0, nslides),
            'nslides': nslides,
            'category': category,
            'carousel_id': f'carousel_{index}',
        })
        product = Product.objects.filter(category=category).first()
        if product:
            category_cards.append({
                'category': category,
                'image': product.image,  
                'product_id': product.product_id,
            })
    return render(request, 'shop/index.html', {'all_products': all_products})

def about(request):
    return render(request, 'shop/about.html')

def contact(request):
    thank = False
    if request.method == "POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        subject = request.POST.get('subject', '')
        message = request.POST.get('message', '')
        contact = Contact(name=name, email=email, subject=subject, message=message)
        contact.save()
        thank = True
        return render(request, 'shop/contact.html', {'thank': thank})
        
    return render(request, 'shop/contact.html')

def tracker(request):
    if request.method == "POST":
        orderId = request.POST.get('orderId', '')
        email = request.POST.get('email', '')
        
        try:
            order = Order.objects.filter(order_id=orderId, email=email)
            if len(order) > 0:
                update = Orderupdate.objects.filter(order_id=orderId)
                updates = []
                for item in update:
                    updates.append({'text': item.update_desc, 'time': item.timestamp})
                    response = json.dumps({"status": "success", "updates": updates, "itemsJson": order[0].items_json}, default=str)
                return HttpResponse(response)
            else:
                return HttpResponse('{"status": "No Item Found with this OrderId!"}')
        except Exception as e:
            return HttpResponse('{"status": "Something Went Wrong!"}')
    return render(request, 'shop/tracker.html')

def searchMatch(query, item):
    query = query.lower()
    return query in item.product_name.lower() or \
           query in item.category.lower()

def search(request):
    query = request.GET.get('search', '').strip()
    searched_products = []

    if query:
        categories = Product.objects.values_list('category', flat=True).distinct()
        for category in categories:
            productTemp = Product.objects.filter(category=category)
            product = [item for item in productTemp if searchMatch(query, item)]
            if product:
                searched_products.append({
                    'products': product,
                    'category': category,
                })

    return render(request, 'shop/search.html', {'searched_products': searched_products})

def productView(request, myid):
    product = Product.objects.get(product_id=myid)
    return render(request, 'shop/product.html', {'product': product})

def checkout(request):
    if request.method == "POST":
        itemsJson = request.POST.get('itemsJson', '')
        amount = request.POST.get('amount', '')
        first_name = request.POST.get('first_name', '')
        last_name = request.POST.get('last_name', '')
        phone = request.POST.get('phone', '')
        email = request.POST.get('email', '')
        address = request.POST.get('address', '')
        district = request.POST.get('district', '')
        province = request.POST.get('province', '')
        zip_code = request.POST.get('zip_code', '')
        
        order = Order(items_json=itemsJson, amount=amount, first_name=first_name, last_name=last_name, phone=phone, email=email, address=address, district=district, province=province, zip_code=zip_code)
        order.save()
        thank = True
        updateOrder = Orderupdate(order_id=order.order_id, update_desc="The order has been placed.")
        updateOrder.save()
        id = order.order_id
        return render(request, 'shop/checkout.html', {'thank': thank, 'id': id})

    return render(request, 'shop/checkout.html')

def category(request, category):
    products = Product.objects.filter(category=category)
    return render(request, 'shop/category.html', {'category': category, 'products': products})


from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages

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

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

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

    # Handle GET request (show the login form)
    return render(request, "login.html")

from django.contrib.auth import logout

def user_logout(request):
    logout(request)
    return redirect('/')