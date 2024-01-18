from django.urls import path
from . import views

app_name="product"
urlpatterns = [
        path("", views.index, name="index"),
        path("order/", views.order, name="order"),
        path("cart/", views.cart, name="cart"),
        ]
