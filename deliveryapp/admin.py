from django.contrib import admin
from .models import Restaurant, Item, Cart, CartItem

# Register your models here.
admin.site.register(Restaurant)
admin.site.register(Item)
admin.site.register(Cart)
admin.site.register(CartItem)