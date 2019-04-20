from django.shortcuts import render, redirect
from .models import Items


def items(request):
    item_list = Items.objects.all().order_by('uploadDate')
    return render(request, 'member/items.html',{'item_list':item_list})

def write(request):
    return render(request,'member/write.html')
