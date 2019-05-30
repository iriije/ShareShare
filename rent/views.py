from django.shortcuts import render, redirect
from .models import Rent
from .forms import RentForm
from item.models import Item 


def rent(request, item_id):
    if request.method == 'POST':
        rent_form = RentForm(request.POST)
        if rent_form.is_valid():
            rent_form = rent_form.save(item_id, request.user)
            return redirect('index')
    else:
        rent_form = RentForm()
    item = Item.objects.get(id = item_id)
    context = {
        'rent_form': rent_form,
        'item': item
    }
    return render(request, 'rent/rent_form.html', context)
