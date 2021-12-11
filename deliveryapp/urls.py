from django.urls import path
from .views import aboutPageView, cartPageView, indexPageView, orderPageView, editItemPageView, restaurantPageView,itemPageView
from .views import submitOrderPageView, newCartPageView, deleteItemPageView, saveItemPageView, addItemPageView

urlpatterns = [
    path("", indexPageView, name='index'),
    path("about/", aboutPageView, name='about'),
    path("order/", orderPageView, name='order'),
    path("cart/", cartPageView, name="cart"),
    path("newcart/", newCartPageView, name="newcart"),
    path("deleteitem/", deleteItemPageView, name="delete-item"),
    path("edititem/<int:cart_item_id>/", editItemPageView, name="cart"),
    path("saveitem/", saveItemPageView, name="save-item"),
    path("restaurant/<int:cart_number>/", restaurantPageView, name="restaurant"),   # Chase will do
    path("item/<int:cart_number>/<int:restaurant_id>/", itemPageView, name="item"), # Chase will do
    path("additem/", addItemPageView, name="add-item"),                             # Chase will do
    path("submitorder/", submitOrderPageView, name="submit-order"),
]