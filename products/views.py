from django.shortcuts import render
from .models import Product


def index(request):
    """
    Displays index page of Product app
    """
    products = Product.objects.all()
    return render(request, "products.html", {"products": products})
