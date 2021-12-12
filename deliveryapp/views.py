from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from deliveryapp.models import Cart

# Create your views here.
def indexPageView(request) :
    return render(request, 'deliveryapp/index.html')

def aboutPageView(request) :
    return render(request, 'deliveryapp/about.html')

def orderPageView(request) :
    context = {
        "failure" : False
    }
    return render(request, 'deliveryapp/order.html', context)

def cartPageView(request, cart_number) :
    cart = Cart.objects.get(id=cart_number)
    restaurants = {}
    for item in cart.items.all() :
        if item.restaurant not in restaurants :
            restaurants[item.restaurant] = {item}
        else :
            restaurants[item.restaurant].add(item)
    
    context = {
        "cart" : cart,
        "restaurants" : restaurants
    }

    return render(request, 'deliveryapp/cart.html', context)

def editItemPageView(request) :
    return render(request, 'deliveryapp/cart.html')

def restaurantPageView(request, cart_number) :
    return render(request, 'deliveryapp/cart.html')

def itemPageView(request) :
    return render(request, 'deliveryapp/cart.html')

def orderSummaryPageView(request) :
    return render(request, 'deliveryapp/ordersummary.html')


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
    try :
        cartid = Cart.objects.get(id=request.GET['inputCartNumber'])
        return redirect('cart', cartid.id)
    except:
        context = {
            "failure" : True,
            "cartNum" : request.GET['inputCartNumber']
        }
        return render(request, 'deliveryapp/order.html', context)