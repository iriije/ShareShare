from django.shortcuts import render, redirect
from .models import Item
from .forms import ItemForm


def items(request):
    item_list = Item.objects.all().order_by('uploadDate')
    return render(request, 'item/items.html',{'item_list':item_list})

def regist(request):
    if request.method == 'POST':
        regist_form = ItemForm(request.POST)
        if regist_form.is_valid():
            item_form = regist_form.save()
            return redirect('/item/item')
    else:
        item_form = ItemForm()

    context = {
        'item_form': item_form,
    }
    return render(request,'item/item_form.html', context)
