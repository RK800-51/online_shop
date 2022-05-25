from django.shortcuts import render
from .models import *
from cart.forms import CartAddProductForm

# Create your views here.
def product(request, product_id :int):
    product = Product.objects.get(id=product_id, is_active=True)
    cart_product_form = CartAddProductForm()
    return render(request, 'products/product.html', locals())