from django.db import models
from django import forms
from django.utils.translation import ugettext_lazy as _

from .models import Item, ItemType


class ItemForm(forms.ModelForm):
    image = forms.ImageField(
        label=_('Image'),
        required=True
    )
    name = forms.CharField(
        label=_('Name'),
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': _('input item name'),
                'required': 'True',
            }
        )
    )
    itemType = forms.ChoiceField(
        label=_('Item Type'),
        required=True,
        widget=forms.Select, 
        choices=ItemType.CATEGORY_CHOICES
    )
    deposit = forms.IntegerField(
        label=_('Deposit'),
        required=True,
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': _('Deposit'),
                'required': 'True',
            }
        )
    )
    rentalFeePerHour = forms.IntegerField(
        label=_('RentalFee'),
        required=True,
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': _('Rental Fee'),
                'required': 'True',
            }
        )
    )
    shippingMethod = forms.CharField(
        label=_('Shipping Method'),
        required=True,
        widget=forms.Select(choices=Item.SHIPPINGMETHOD_CHOICES)
    )
    location = forms.CharField(
        label=_('Location'),
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': _('input location'),
                'required': 'True',
            }
        )
    )
    maxRentTime = forms.IntegerField(
        label=_('RentTime'),
        required=True,
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': _('Rent Time'),
                'required': 'True',
            }
        )
    )
    explanation = forms.CharField(
        label=_('Explanation'),
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': _('Explain your item'),
                'required': 'True',
            }
        )
    )

    class Meta:
        model = Item
        fields = ('image', 'name', 'itemType', 'deposit', 'rentalFeePerHour', 'shippingMethod', 'location', 'maxRentTime', 'explanation',)

    def save(self, user, commit=True):
        item = super(ItemForm, self).save(commit=False)
        item.user = user
        if commit:
            item.save()
        return item

class ItemUpdateForm(forms.Form):
    name = forms.CharField(
        label=_('Name'),
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': _('input item name'),
                'required': 'True',
            }
        )
    )
    deposit = forms.IntegerField(
        label=_('Deposit'),
        required=True,
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': _('Deposit'),
                'required': 'True',
            }
        )
    )
    rentalFeePerHour = forms.IntegerField(
        label=_('RentalFee'),
        required=True,
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': _('Rental Fee'),
                'required': 'True',
            }
        )
    )
    shippingMethod = forms.CharField(
        label=_('Shipping Method'),
        required=True,
        widget=forms.Select(choices=Item.SHIPPINGMETHOD_CHOICES)
    )
    location = forms.CharField(
        label=_('Location'),
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': _('input location'),
                'required': 'True',
            }
        )
    )
    maxRentTime = forms.IntegerField(
        label=_('RentTime'),
        required=True,
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': _('Rent Time'),
                'required': 'True',
            }
        )
    )
    explanation = forms.CharField(
        label=_('Explanation'),
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': _('Explain your item'),
                'required': 'True',
            }
        )
    )


class SearchForm(forms.Form):
    word = forms.CharField(label='')

class SortForm(forms.Form):
    startDateTime = forms.DateTimeField(
        label=_('Start Date Time'),
        required=True,
        input_formats=['%Y-%m-%dT%H:%M'],
        widget=forms.DateTimeInput(
            attrs={
                'class': 'form-control',
                'placeholder': _('Start Date Time'),
                'required': 'True',
                'type': 'datetime-local'
            }
        )
    )
    endDateTime = forms.DateTimeField(
        label=_('End Date Time'),
        required=True,
        input_formats=['%Y-%m-%dT%H:%M'],
        widget=forms.DateTimeInput(
            attrs={
                'class': 'form-control',
                'placeholder': _('End Date Time'),
                'required': 'True',
                'type': 'datetime-local'
            }
        )
    )

    

