from django.shortcuts import render
from products.models import Product
from django.db.models import Q


def search_index(request):
    """
    Search within the Products
    """
    query =None
    products = None

    if 'q' in request.GET:
        query = request.GET.get('q')
        products = Product.objects.all().filter(Q(name__icontains=query) | Q(description__icontains=query))

    return render(request, "products.html", {"products": products})