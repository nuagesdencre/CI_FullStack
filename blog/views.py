from django.shortcuts import render


def blog(request):
    """
    Display the main blog page
    """
    return render(request, 'blog.html')