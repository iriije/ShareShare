from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from django.db.models import Q

from item.models import Item
from item.forms import SearchForm

from rent.models import Rent
  
def index(request):
    if request.method == 'POST':
        search_form = SearchForm(request.POST)
        if search_form.is_valid():
            word = '%s' %request.POST['word']
        item_list = Item.objects.filter(
            Q(name__icontains=word) | Q(explanation__icontains=word)
        ).distinct()
        context = {
            'item_list': item_list,
            'search_word': word
        }
        return render(request, 'item/items.html', context)
    
    else:
        search_form = SearchForm()

        if request.user:
            rent_list = Rent.objects.filter(
                Q(sharee__nickname=request.user.nickname)
            )
            tag_list = []
            for rent in rent_list:
                print(rent.item.name)
                tag_list += rent.item.tag_set.all()
            
    
            if len(tag_list)>0:
                tag = max(set(tag_list), key=tag_list.count)
                item_list = Item.objects.filter(tag__name=tag.name)
            else:
                item_list = []

    context = {
        'search_form': search_form,
        'item_list': item_list,
    }
    template = loader.get_template('main/index.html')

    return HttpResponse(template.render(context, request))

	
