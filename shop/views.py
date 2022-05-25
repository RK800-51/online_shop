from django.shortcuts import render, get_object_or_404
from products.models import Product, ProductCategory, ProductImage


def product_list(request, category_id=None):
    category = None
    categories = ProductCategory.objects.all()
    products = Product.objects.filter(is_active=True)
    if category_id:
        category = get_object_or_404(ProductCategory, id=category_id)
        products = products.filter(category=category)
    return render(request, 'shop/product_list.html', locals())
