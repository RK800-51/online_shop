from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('', product_list, name='product_list'),
    path('<int:category_id>', product_list, name='product_list_by_category'),


]