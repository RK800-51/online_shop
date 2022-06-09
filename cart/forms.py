from django import forms

PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]


class CartAddProductForm(forms.Form):
    quantity = forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICES, coerce=int)
    #update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)
    #cart_product = forms.DecimalField(required=False, widget=forms.HiddenInput)

class CheckoutForm(forms.Form):
    name = forms.CharField(required=True, max_length=50)
    phone = forms.CharField(required=True, max_length=50)