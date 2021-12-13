from django.urls import path
from .views import aboutPageView, cartPageView, indexPageView, orderPageView, editItemPageView, restaurantPageView,itemPageView
from .views import orderSummaryPageView, newCartPageView, deleteItemPageView, saveItemPageView, addItemPageView, findCart

urlpatterns = [
    path("", indexPageView, name='index'),
    path("about/", aboutPageView, name='about'),
    path("order/", orderPageView, name='order'),
    path("cart/<int:cart_number>/", cartPageView, name="cart"),
    path("newcart/", newCartPageView, name="newcart"),
    path("deleteitem/", deleteItemPageView, name="delete-item"),
    path("edititem/<int:cart_item_id>/", editItemPageView, name="edit-item"),
    path("saveitem/<int:cart_item_id>", saveItemPageView, name="save-item"),
    path("restaurant/<int:cart_number>/", restaurantPageView, name="restaurant"),   
    path("item/<int:cart_number>/<int:restaurant_id>/", itemPageView, name="item"), 
    path("additem/", addItemPageView, name="add-item"),                             
    path("ordersummary/<int:cart_number>/", orderSummaryPageView, name="ordersummary"),
    path("findcart/", findCart, name="find-cart")
]