from django import forms
from .models import Product, Inbound, Outbound

class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ('code', 'name', 'description','price','size')

    widgets = {
        'code': forms.TextInput(attrs={'class': 'form-control'}),
        'name': forms.TextInput(attrs={'class': 'form-control'}),
        'description': forms.TextInput(attrs={'class': 'form-control'}),
        'price': forms.TextInput(attrs={'class': 'form-control'}),
        'size': forms.Select(attrs={'class': 'form-control'}),
    }
    labels = {
        'code': 'Code',
        'name': 'Name',
        'description': 'Description',
        'price': 'Price',
        'size': 'Size',
    }


class InboundForm(forms.ModelForm):

    class Meta:
        model = Inbound
        fields = ('code', 'quantity','price','size')

    widgets = {
        'code': forms.TextInput(attrs={'class': 'form-control'}),
        'size': forms.Select(attrs={'class': 'form-control'}),
        'quantity': forms.TextInput(attrs={'class': 'form-control'}),
        'price': forms.TextInput(attrs={'class': 'form-control'}),
    }
    labels = {
        'code': 'Code',
        'size': 'Size',
        'quantity': 'quantity',
        'price': 'Price',
    }

class OutboundForm(forms.ModelForm):
    class Meta:
        model = Outbound
        fields = ('code', 'out_quantity', 'price','size')

    widgets = {
        'code': forms.TextInput(attrs={'class': 'form-control'}),
        'size': forms.Select(attrs={'class': 'form-control'}),
        'out_quantity': forms.TextInput(attrs={'class': 'form-control'}),
        'price': forms.TextInput(attrs={'class': 'form-control'}),
    }
    labels = {
        'code': 'Code',
        'size': 'Size',
        'out_quantity': 'out_quantity',
        'price': 'Price',
    }