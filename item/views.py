import boto3

from django.shortcuts import render, redirect
from .models import Item, Tag
from .forms import ItemForm, SearchForm, SortForm
from django.views.generic.edit import FormView
from django.db.models import Q
from rent.models import Rent
import datetime


def items(request):
    if request.method == 'POST':
        sort_form = SortForm(request.POST)
        if sort_form.is_valid():
            startDate = request.POST['startDate']
            endDate = request.POST['endDate']

            rent_list = Rent.objects.filter(
                Q(rentDate__range=(startDate, endDate)) | Q(dueDate__range=(startDate, endDate))
            ).distinct()
            rentItemId_list = []

            for rent in rent_list:
                rentItemId_list.append(rent.item.id)

            item_list = Item.objects.all().order_by('uploadDate').exclude(id__in=rentItemId_list)

            context = {
                'item_list':item_list,
                'sort_form':sort_form
            }
            return render(request, 'item/items.html', context)
        else:
            item_list = Item.objects.all().order_by('uploadDate')
            sort_form = SortForm()

    else:
        sort_form = SortForm()
        item_list = Item.objects.all().order_by('uploadDate')
    
    context = {
        'sort_form': sort_form,
        'item_list': item_list
    }
    
    return render(request, 'item/items.html', context)

def regist(request):
    if request.method == 'POST':
        item_form = ItemForm(request.POST, request.FILES)
        if item_form.is_valid():
            item = item_form.save(request.user)
            tags = []
            imageFile=item.image.path
            client=boto3.client('rekognition')
            with open(imageFile, 'rb') as image:
                response = client.detect_labels(Image={'Bytes': image.read()})
            for label in response['Labels']:
                tags.append(label['Name'])
            if tags:
                for tag in tags:
                    tag = Tag.objects.get_or_create(name=tag)
                    item.tag_set.add(tag)
        
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