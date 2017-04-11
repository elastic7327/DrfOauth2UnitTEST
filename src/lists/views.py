from django.shortcuts import render
from django.http import HttpResponse

from rest_framework import generics, status
from rest_framework.response import Response


# Create your views here.

def home_page(request):
    """TODO: Docstring for home_page.

    :arg1: TODO
    :returns: TODO

    """
    return HttpResponse("Hello World")
