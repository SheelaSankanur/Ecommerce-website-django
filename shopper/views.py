from django.shortcuts import render
import json
from shop.models import Product

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