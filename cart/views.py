from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from products.models import Product, ProductImage
from .cart import Cart
from .forms import CartAddProductForm, CheckoutForm
from orders.models import Order, ProductInOrder
from django.http import HttpResponse, HttpResponseRedirect



@require_POST
def cart_add(request, product_id:int):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product,
                  quantity=cd['quantity'])
    print(cart.cart.keys())
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
        print(cart.cart.keys())
        if form.is_valid():
            data = request.POST
            phone = data['phone']
            name = data['name']
            user, created = User.objects.get_or_create(username=phone,
                                              first_name=name)
            order = Order.objects.create(user=user, customer_name=name,
                                         customer_phone=phone, status_id=1)
            for product in cart:
                item = ProductInOrder.objects.create(order=order,
                                                     session_key=session_key,
                                                     product_id=product['product_id'],
                                                     nmb=product['quantity'],
                                                     price_per_item=product['product_price'],
                                                     total_price=product['total_price'])


        else:
            print('no')
        cart.clear()
        return render(request, 'cart/checkout.html', locals())
