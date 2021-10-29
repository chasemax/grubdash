from django.urls import path
from .views import indexPageView, contactPageView, orderPageView

urlpatterns = [
    path("", indexPageView, name='Home'),
    path("contact/", contactPageView, name='Contact'),
    path("order/", orderPageView, name='Order'),
]