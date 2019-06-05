from django.db import models
from django import forms
from django.utils.translation import ugettext_lazy as _
from item.models import Item

from datetime import datetime, timedelta

from .models import Rent


class RentForm(forms.ModelForm):
    rentDateTime = forms.DateTimeField(
        label=_('Rent Date Time'),
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
    
    dueDateTime = forms.DateTimeField(
        label=_('Due Date Time'),
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


    class Meta:
        model = Rent
        fields = ('rentDateTime', 'dueDateTime')

    def save(self, item_id, user, commit=True):
        rent = super(RentForm, self).save(commit=False)
        item = Item.objects.get(id = item_id)
        rent.item = item
        rent.sharee = user
        user.point -= item.rentalFeePerHour * int((rent.dueDateTime - rent.rentDateTime).seconds / 3600)

        if commit:
            rent.save()
            user.save()
        return rent