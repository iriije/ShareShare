from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.db.models import Q

from item.models import Item, Tag
from item.forms import SearchForm
from rent.models import Rent
from rnn.rnn import RNN
  
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
        rent_list = []
        if request.user.is_authenticated:
            rent_list = Rent.objects.filter(
                Q(sharee__nickname=request.user.nickname)
            )
        tag_list = []
        for rent in rent_list:
            tag_list += rent.item.tag_set.all()

        if len(tag_list) > 0:
            tag = max(set(tag_list), key=tag_list.count)
            item_list = Item.objects.filter(tag_set__in=[tag])
        else:
            item_list = []

    context = {
        'search_form': search_form,
        'item_list': item_list,
    }
    template = loader.get_template('main/index.html')

    return HttpResponse(template.render(context, request))


def recommend(request):
    item_list = []
    if request.user.is_authenticated:
        rent_list = Rent.objects.filter(
            Q(sharee__nickname=request.user.nickname)
        )
        tag_list = []
        for rent in rent_list:
            tag_list += rent.item.tag_set.all()
        input_tags = []
        if len(tag_list) > 0:
            for i in range(min(3, len(tag_list))):
                tag = max(set(tag_list), key=tag_list.count)
                input_tags.append(tag.name)
                tag_list.remove(tag)
        if len(input_tags) > 0: 
            rnn = RNN()
            res = rnn.test(input_tags)
            res_tag = res[0]
            item_list = Item.objects.filter(tag_set__in=[Tag.objects.get(name=res_tag)])

    context = {
        'item_list': item_list,
    }
    template = loader.get_template('main/index.html')

    return HttpResponse(template.render(context, request))
    
	
