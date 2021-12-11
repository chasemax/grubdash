from django.db import models
from django.db.models.fields.related import ForeignKey

# Create your models here.

class Restaurant(models.Model) :

    name = models.CharField(max_length=30)
    addressline1 = models.CharField(max_length=100)
    addressline2 = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=2)
    zip = models.CharField(max_length=10)
    phone = models.CharField(max_length=10)

    def __str__(self) :
        return (self.name)

class Item(models.Model) :

    name = models.CharField(max_length=30)
    description = models.CharField(max_length=255)
    cost = models.DecimalField(max_digits=5, decimal_places=2)
    isactive = models.BooleanField()
    restaurant = models.ForeignKey(Restaurant, models.CASCADE)

    def __str__(self) :
        return (self.name)

class Cart(models.Model) :

    customerfirstname = models.CharField(max_length=20)
    customerlastname = models.CharField(max_length=30)
    customerphone = models.CharField(max_length=10)

    deliveryaddressline1 = models.CharField(max_length=100)
    deliveryaddressline2 = models.CharField(max_length=100, blank=True)
    deliverycity = models.CharField(max_length=30)
    deliverystate = models.CharField(max_length=2)
    deliveryzip = models.CharField(max_length=10)
    
    cardnumber = models.CharField(max_length=16)
    cardexpiration = models.DateField(null=True, blank=True)
    cardcvv = models.CharField(max_length=3)

    items = models.ManyToManyField('Item', through='CartItem')

    @property
    def cartname(self) :
        return (self.customerfirstname + ' ' + self.customerlastname + "'s cart")

    def __str__(self) :
        return self.cartname


class CartItem(models.Model) :

    cart = ForeignKey(Cart, on_delete=models.CASCADE)
    item = ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self) :
        return (self.cart.cartname + ': ' + self.item.name)
