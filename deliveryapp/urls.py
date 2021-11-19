from django.urls import path
from .views import aboutPageView, cartPageView, indexPageView, orderPageView

urlpatterns = [
    path("", indexPageView, name='index'),
    path("about/", aboutPageView, name='about'),
    path("order/", orderPageView, name='order'),
    path("cart/", cartPageView, name="cart")
]