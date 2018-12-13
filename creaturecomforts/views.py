from django.shortcuts import render_to_response


def handler404(request, exception, template_name="404.html"):
    """
    Display with an error message.
    A 404 error is returned by a web server (the machine where a website is hosted)
    when it cannot find the page requested
    """
    response = render_to_response("404.html")
    response.status_code = 404
    return response


def handler500(request, exception, template_name="500.html"):
    """
    Display a page with an error message.
    The 500 Internal Server Error is a very general HTTP status code
    that means something has gone wrong on the website's server.
    """
    response = render_to_response("500.html")
    response.status_code = 500
    return response
