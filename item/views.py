from django.shortcuts import render, redirect
from .models import Item
from .forms import ItemForm, SearchForm, SortForm
from django.views.generic.edit import FormView
from django.db.models import Q
from rent.models import Rent
import datetime


def items(request):
    item_list = Item.objects.all().order_by('uploadDate')
    return render(request, 'item/items.html',{'item_list':item_list})

def regist(request):
    if request.method == 'POST':
        item_form = ItemForm(request.POST, request.FILES)
        if item_form.is_valid():
            item_form.save(request.user)
            return redirect('/item/items')
    else:
        item_form = ItemForm()

    context = {
        'item_form': item_form,
    }
    return render(request,'item/item_form.html', context)


class SearchFormView(FormView):
    form_class = SearchForm
    template_name = 'main/index.html'

    def form_valid(self, form):
        word = '%s' %self.request.POST['word']
        item_list = Item.objects.filter(
            Q(name__icontains=word) | Q(explanation__icontains=word)
        ).distinct()
        context = {
            'item_list': item_list,
            'search_word': word
        }
        return render(self.request, 'item/items.html', context)

class SortFormView(FormView):
    form_class = SortForm
    template_name = 'item/items.html'
    item_list = Item.objects.all().order_by('uploadDate')

    def form_valid(self, form):
        startDate = self.request.POST['startDate']
        endDate = self.request.POST['endDate']

        item_list = []
        rent_list = Rent.objects.exclude(
            rentDate__range=(startDate, endDate)
        ).exclude(
            duedate__range=(startDate, endDate)
        )

        for rent in rent_list:
            item_list.append(rent.item)

        context = {
            'item_list': item_list
        }
        return render(self.request, 'item/items.html', context)
        

