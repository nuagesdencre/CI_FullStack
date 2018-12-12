from django.shortcuts import render
from products.models import Product
from django.db.models import Q



def search_index(request):
    """
    Search within the Products
    """
    query = None
    products = None
    all_products = True
    if 'q' in request.GET:
        query = request.GET.get('q')
        products = Product.objects.all().filter(Q(name__icontains=query) | Q(description__icontains=query))
        all_products = False

    return render(request, "products.html", {"products": products, "all_products": all_products})
