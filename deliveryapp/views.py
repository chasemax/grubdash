from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.
def indexPageView(request) :
    return HttpResponse("This is the home page")

def contactPageView(request) :
    return HttpResponse("This is the page where users find contact information for the company")

def orderPageView(request) :
    return HttpResponse("This is where the user puts in their orders")