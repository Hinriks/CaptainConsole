from django.forms import ModelForm, widgets
from django import forms
from product.models import Product

class ProductUpdateForm(ModelForm):
    class Meta:
        model = Product
        exclude = [ 'id' ]
        widgets = {
            'name': widgets.TextInput(attrs={ 'class': 'form-control' }),
            'description': widgets.TextInput(attrs={ 'class': 'form-control' }),
            'category': widgets.Select(attrs={ 'class': 'form-control' }),
            'price': widgets.NumberInput(attrs={ 'class': 'form-control' }),
            'manufacturer': widgets.Select(attrs={ 'class': 'form-control' }),
        }

class ProductCreateForm(ModelForm):
    image = forms.CharField(required=True, widget=forms.TextInput(attrs={ 'class': 'form-control' }))
    class Meta:
        model = Product
        exclude = [ 'id' ]
        widgets = {
            'name': widgets.TextInput(attrs={ 'class': 'form-control' }),
            'description': widgets.TextInput(attrs={ 'class': 'form-control' }),
            'category': widgets.Select(attrs={ 'class': 'form-control' }),
            'price': widgets.NumberInput(attrs={ 'class': 'form-control' }),
            'manufacturer': widgets.Select(attrs={ 'class': 'form-control' }),
        }