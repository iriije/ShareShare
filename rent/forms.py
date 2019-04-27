from django.db import models
from django import forms
from django.utils.translation import ugettext_lazy as _
from item.models import Item

from .models import Rent


class RentForm(forms.ModelForm):
    rentDate = forms.DateField(
        label=_('Rent Date'),
        required=True,
        widget=forms.DateInput(
            attrs={
                'class': 'form-control',
                'placeholder': _('Start Date'),
                'required': 'True',
                'type': 'date'
            }
        )
    )
    rentTime = forms.TimeField(
        label=_('Rent Time'),
        required=True,
        widget=forms.TimeInput(
            attrs={
                'class': 'form-control',
                'placeholder': _('Start Time'),
                'required': 'True',
                'type': 'time'
            }
        )
    )
    dueDate = forms.DateField(
        label=_('Due Date'),
        required=True,
        widget=forms.DateInput(
            attrs={
                'class': 'form-control',
                'placeholder': _('End Date'),
                'required': 'True',
                'type': 'date'
            }
        )
    )
    dueTime = forms.TimeField(
        label=_('Due Time'),
        required=True,
        widget=forms.TimeInput(
            attrs={
                'class': 'form-control',
                'placeholder': _('End Time'),
                'required': 'True',
                'type': 'time'
            }
        )
    )

    class Meta:
        model = Rent
        fields = ('rentDate', 'rentTime', 'dueDate', 'dueTime')

    def save(self, item_id, user, commit=True):
        rent = super(RentForm, self).save(commit=False)
        item = Item.objects.get(id = item_id)
        rent.item = item
        rent.sharee = user
        if commit:
            rent.save()
        return rent