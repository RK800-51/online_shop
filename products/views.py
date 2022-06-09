from django.shortcuts import render
from .models import *
from cart.forms import CartAddProductForm


def product(request, product_id :int):
    product = Product.objects.get(id=product_id, is_active=True)
    cart_product_form = CartAddProductForm()
    session_key = request.session.session_key
    if not session_key:
        request.session.cycle_key()
    return render(request, 'products/product.html', locals())

