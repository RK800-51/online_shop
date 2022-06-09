from django.contrib import admin
from django.urls import path, include
from .views import *


app_name = 'cart'
urlpatterns = [
    path('', cart_detail, name='cart_detail'),
    path('checkout', checkout, name='checkout'),
    path('add/<int:product_id>', cart_add, name='cart_add'),
    path('remove/<int:product_id>', cart_remove, name='cart_remove'),
]