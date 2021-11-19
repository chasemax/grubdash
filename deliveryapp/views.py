from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.
def indexPageView(request) :
    return render(request, 'deliveryapp/index.html')

def aboutPageView(request) :
    return render(request, 'deliveryapp/about.html')

def orderPageView(request) :
    return render(request, 'deliveryapp/order.html')

def cartPageView(request) :
    return render(request, 'deliveryapp/cart.html')