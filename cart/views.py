from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from products.models import Product, ProductImage
from cart.models import CartModel
from .cart import Cart
from .forms import CartAddProductForm, CheckoutForm
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse


@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product,
                  quantity=cd['quantity'])
    return redirect('cart:cart_detail')

def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart:cart_detail')

def cart_detail(request):
    cart = Cart(request)
    return render(request, 'cart/detail.html', locals())

def checkout(request):
    session_key = request.session.session_key
    cart = Cart(request)
    form = CheckoutForm(request.POST)
    if request.POST:
        print(request.POST)
        if form.is_valid():
            print('yes')
        else:
            print('no')
        return render(request, 'cart/detail.html', locals())
