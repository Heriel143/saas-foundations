from django.shortcuts import render
from visits.models import PageVisits


def home_page(request, *aegs, **kwargs):
    queryset = PageVisits.objects.all()
    my_title = "My Page"
    my_context = {"page_title": my_title, "page_visits": queryset}

    html_template = "home.html"

    PageVisits.objects.create(path=request.path)
    return render(request, html_template, my_context)
