from django.shortcuts import render
from products.models import Product

def search_index(request):
    """
    Search within the Products
    """
    products = Product.objects.filter(name__icontains=request.GET['q'])

    return render(request, "products.html", {"products": products})