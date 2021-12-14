from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from deliveryapp.models import Cart, Restaurant, Item, CartItem
from datetime import datetime
# Create your views here
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
    
    cartItems = cart.cartitem_set.all()
    total = 0
    for item in cartItems :
        total = total + (item.quantity * item.item.cost)
    
    context = {
        "cart" : cart,
        "restaurants" : restaurants,

        "items" : cartItems,
        "total" : total
        
    }

    return render(request, 'deliveryapp/cart.html', context)

def editItemPageView(request, cart_item_id) :
    cartItem = CartItem.objects.get(id=cart_item_id)
    context = {
        'cartItem' : cartItem
    }
    return render(request, 'deliveryapp/edit.html', context)
    

def restaurantPageView(request, cart_number) :

    all_restaurants = Restaurant.objects.all()

    context = {
        'all_restaurants': all_restaurants,
        'cart_number': cart_number
    }

    return render(request, 'deliveryapp/restaurant.html', context)

def itemPageView(request, cart_number, restaurant_id) :

    current_restaurant = Restaurant.objects.get(id=restaurant_id)

    all_items = Item.objects.filter(isactive=True, restaurant=current_restaurant)

    context = {
        'all_items': all_items,
        'current_restaurant': current_restaurant,
        'cart_number': cart_number
    }

    return render(request, 'deliveryapp/item.html', context)

def orderSummaryPageView(request, cart_number) :
    if request.method == 'POST' :
        cart = Cart.objects.get(id=cart_number)
        items = cart.cartitem_set.all()
        total = 0
        all_items = list()
        for item in items:
            all_items.append({'name' : item.item.name, 'quantity' : item.quantity, 'unit_price' : item.item.cost, 'total_price' : item.item.cost * item.quantity})
            total += item.quantity * item.item.cost
        month = request.POST['month']
        year = request.POST['year']
        expiration = ('20' + str(year) + '-' + str(month) + '-01')

        cart.customerfirstname = request.POST['customerfirstname']
        cart.customerlastname = request.POST['customerlastname']
        cart.customerphone = request.POST['customerphone']
        cart.deliveryaddressline1 = request.POST['deliveryaddressline1']
        cart.deliveryaddressline2 = request.POST['deliveryaddressline2']
        cart.deliverycity = request.POST['deliverycity']
        cart.deliverystate = request.POST['deliverystate'].upper()
        cart.deliveryzip = request.POST['deliveryzip']
        cart.cardnumber = request.POST['cardnumber']
        cart.cardexpiration = expiration
        cart.cardcvv = request.POST['cardcvv']

        cart.save()

        name = cart.customerfirstname + " " + cart.customerlastname

        context = {
            "name" : name,
            "cart_number" : cart_number,
            "date" : datetime.now(),
            "all_items" : all_items,
            "total" : total
        }
        
        return render(request, 'deliveryapp/ordersummary.html',context)


def newCartPageView(request) :
    newCart = Cart.objects.create()

    newCartNum = newCart.id

    return redirect('restaurant', newCartNum)

def deleteItemPageView(request, cart_item_id) :
    cartID = CartItem.objects.get(id=cart_item_id).cart.id
    CartItem.objects.get(id=cart_item_id).delete()
    return redirect('cart', cartID)

def saveItemPageView(request, cart_item_id) :
    cartItem = CartItem.objects.get(id=cart_item_id)
    cartItem.quantity = request.POST['inputQuantity']
    cartItem.save()
    return redirect('cart', cartItem.cart.id)
    
    

def addItemPageView(request) :

    cart_number = request.POST['cart_number']
    item_id = request.POST['item_id']
    quantity = request.POST['quantity']

    cart = Cart.objects.get(id=cart_number)
    item = Item.objects.get(id=item_id)

    cart_item = CartItem()
    cart_item.cart = cart
    cart_item.item = item
    cart_item.quantity = quantity

    cart_item.save()

    return redirect('cart', cart_number=cart_number)

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