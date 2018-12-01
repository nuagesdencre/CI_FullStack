from django.shortcuts import render, redirect, reverse, render_to_response


def handler404(request, exception, template_name="404.html"):
    """
    Error view
    """
    response = render_to_response("404.html")
    response.status_code = 404
    return response


def handler500(request, exception, template_name="500.html"):
    """
    Error view
    """
    response = render_to_response("500.html")
    response.status_code = 500
    return response
