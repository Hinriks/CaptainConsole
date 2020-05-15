from django.forms import ModelForm
from django import forms
from user.models import Order

class CompleteOrderForm(ModelForm):
    class Meta:
        model = Order
        exclude = [ 'cart', 'is_ordered',  ]
        fields = (
            'full_name',
            'email',
            'phone_number',
            'address',
            'apt',
            'city',
            'zip',
            'country',
            'card_name',
            'card_number',
            'card_cvc',
            'card_exp_month',
            'card_exp_year',
        )


