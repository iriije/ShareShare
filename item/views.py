import boto3

from django.shortcuts import render, redirect
from .models import Item, Tag
from .forms import ItemForm, ItemUpdateForm, SearchForm, SortForm
from django.views.generic.edit import FormView
from django.db.models import Q
from rent.models import Rent
import datetime


def items(request):
    if request.method == 'POST':
        sort_form = SortForm(request.POST)
        if sort_form.is_valid():
            startDateTime = request.POST['startDateTime']
            endDateTime = request.POST['endDateTime']

            rent_list = Rent.objects.filter(
                Q(rentDateTime__range=(startDateTime, endDateTime)) | Q(dueDateTime__range=(startDateTime, endDateTime))
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
                if float(label['Confidence']) > 0:
                    tags.append(label['Name'])
            if tags:
                for tag in tags:
                    tag_obj, created = Tag.objects.get_or_create(name=tag)
                    item.tag_set.add(tag_obj)
        
            return redirect('/item/items')
    else:
        item_form = ItemForm()

    context = {
        'item_form': item_form,
    }
    return render(request,'item/item_form.html', context)

def update(request, item_id):
    item = Item.objects.get(id=item_id)
    if request.method == 'POST':
        item_update_form = ItemUpdateForm(request.POST)
        if item_update_form.is_valid():
            item.name = item_update_form.cleaned_data['name']
            item.deposit = item_update_form.cleaned_data['deposit']
            item.rentalFeePerHour = item_update_form.cleaned_data['rentalFeePerHour']
            item.shippingMethod = item_update_form.cleaned_data['shippingMethod']
            item.location = item_update_form.cleaned_data['location']
            item.maxRentTime = item_update_form.cleaned_data['maxRentTime']
            item.explanation = item_update_form.cleaned_data['explanation']
            item.save()
        
            return redirect('/member/mypage')
    else:
        item_update_form = ItemUpdateForm()

    context = {
        'item_update_form': item_update_form,
        'item_id': item_id,
    }
    return render(request,'item/item_update_form.html', context)

def delete(request, item_id):
    item = Item.objects.get(id=item_id)
    if request.user.nickname==item.user.nickname:
        item.delete()


def search_tag(request, tag_name):
    item_list = Item.objects.filter(tag_set__in=[Tag.objects.get(name=tag_name)])
    context = {
        'tag_name': tag_name,
        'item_list': item_list,
    }
    return render(request, 'item/item_list_by_tag.html', context)