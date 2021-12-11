from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from deliveryapp.models import Cart

# Create your views here.
def indexPageView(request) :
    return render(request, 'deliveryapp/index.html')

def aboutPageView(request) :
    return render(request, 'deliveryapp/about.html')

def orderPageView(request) :
    return render(request, 'deliveryapp/order.html')

def cartPageView(request, cart_number) :
    context = {
        "cart" : Cart.objects.get(id=cart_number)
    }


    return render(request, 'deliveryapp/cart.html', context)




def editItemPageView(request) :
    return render(request, 'deliveryapp/cart.html')

def restaurantPageView(request, cart_number) :
    return render(request, 'deliveryapp/cart.html')

def itemPageView(request) :
    return render(request, 'deliveryapp/cart.html')

def submitOrderPageView(request) :
    return render(request, 'deliveryapp/cart.html')


def newCartPageView(request) :
    newCart = Cart.objects.create()

    newCartNum = newCart.id

    return redirect('restaurant', newCartNum)

def deleteItemPageView(request) :
    return redirect('cart')

def saveItemPageView(request) :
    return redirect('cart')

def addItemPageView(request) :
    return redirect('cart')

def findCart(request) :
    cartid = Cart.objects.get(id=request.GET['inputCartNumber'])
    return redirect('cart', cartid.id)