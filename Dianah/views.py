from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def home_view(request):
    return HttpResponse("Welcome to the home page!")


def custom_view(request):
    return HttpResponse("This is the custom view.")
