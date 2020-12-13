from django.urls import path
from . import views

urlpatterns = [
    path('', views.order, name = "order"),
    path('checkout/', views.checkout, name = "checkout"),
    path('cart/', views.cart, name = "cart"),
]