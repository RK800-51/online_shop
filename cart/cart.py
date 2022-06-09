from decimal import Decimal
from django.conf import settings
from products.models import Product, ProductImage


class Cart:

    def __init__(self, request):
        """
        Инициализируем корзину
        """
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            # save an empty cart in the session
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def add(self, product, quantity):
        # add product to cart or update its quantity
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': 0, 'price': str(product.price)}
        self.cart[product_id]['quantity'] += quantity
        self.save()

    def save(self):
        # update cart session
        self.session[settings.CART_SESSION_ID] = self.cart
        # mark session as modified to be sured it was saved
        self.session.modified = True

    def remove(self, product):
        # deleting product from cart
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def __iter__(self):
        # iterating elements in cart and getting products from BD
        product_ids = self.cart.keys()
        # getting product objects and adding them to cart
        products = Product.objects.filter(id__in=product_ids)
        for product in products:
            self.cart[str(product.id)]['product_name'] = product.name
            self.cart[str(product.id)]['product_price'] = float(product.price)
            self.cart[str(product.id)]['product_id'] = int(product.id)
            self.cart[str(product.id)]['product_image'] = ProductImage.objects.filter(product=product).first()

        for item in self.cart.values():
            item['product_price'] = float(item['product_price'])
            item['total_price'] = float(item['product_price'] * item['quantity'])
            item['product_id'] = int(item['product_id'])
            yield item

    def __len__(self):
        # counting all products in cart
        return sum(item['quantity'] for item in self.cart.values())

    def get_total_price(self):
        # total price of all products
        return sum(Decimal(item['price']) * item['quantity'] for item in
                   self.cart.values())

    def get_total_amount(self):
        # total amount of products
        return sum(Decimal(item['quantity']) for item in self.cart.values())

    def clear(self):
        # deleting cart from session
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True


