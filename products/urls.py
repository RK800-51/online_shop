from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('/<int:product_id>', product, name='product'),

]