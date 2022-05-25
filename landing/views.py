from django.shortcuts import render
from datetime import datetime
from .forms import SubscribeForm
from products.models import Product, ProductImage

# Create your views here.

def landing(request):
    name = 'RK800'
    current_day = datetime.now()
    form = SubscribeForm(request.POST or None)
    new_form = form.save()
    return render(request, 'landing/landing.html', locals())


def home(request):
    products_images = ProductImage.objects.filter(is_active=True, is_main=True, product__is_active=True)
    products_images_phones = products_images.filter(product__category__id=1)
    product_images_laptops = products_images.filter(product__category__id=2)
    product_images_tablets = products_images.filter(product__category__id=3)
    return render(request, 'landing/home.html', locals())