from django import forms
from .models import Order

class OrderForm(forms.ModelForm):
    order_price = forms.DecimalField(
        label='Total Price',
        disabled=True,
        required=False,
    )

    class Meta:
        model = Order
        fields = ['order_price']  # Add other fields as needed
