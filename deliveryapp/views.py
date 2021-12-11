from django.http.response import HttpResponse
from django.shortcuts import redirect, render

# Create your views here.
def indexPageView(request) :
    return render(request, 'deliveryapp/index.html')

def aboutPageView(request) :
    return render(request, 'deliveryapp/about.html')

def orderPageView(request) :
    return render(request, 'deliveryapp/order.html')

def cartPageView(request) :
    return render(request, 'deliveryapp/cart.html')




def editItemPageView(request) :
    return render(request, 'deliveryapp/cart.html')

def restaurantPageView(request) :
    return render(request, 'deliveryapp/cart.html')

def itemPageView(request) :
    return render(request, 'deliveryapp/cart.html')

def submitOrderPageView(request) :
    return render(request, 'deliveryapp/cart.html')


def newCartPageView(request) :
    return redirect('cart', cart_number=x)

def deleteItemPageView(request) :
    return redirect('cart')

def saveItemPageView(request) :
    return redirect('cart')

def addItemPageView(request) :
    return redirect('cart')