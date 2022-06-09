from django.db import models
from products.models import Product


class CartModel(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return f'Корзина'