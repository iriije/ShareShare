from django.shortcuts import render, redirect
from .models import Rent
from .forms import RentForm


def rent(request, item):
    if request.method == 'POST':
        rent_form = RentForm(request.POST)
        if rent_form.is_valid():
            rent_form = rent_form.save(item, request.user)
            return redirect('index')
    else:
        rent_form = RentForm()

    context = {
        'rent_form': rent_form,
    }
    return render(request, 'rent/rent_form.html', context)
