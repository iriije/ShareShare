from django.shortcuts import render, redirect
from .models import Item
from .forms import ItemForm, SearchForm
from django.views.generic.edit import FormView
from django.db.models import Q


def items(request):
    item_list = Item.objects.all().order_by('uploadDate')
    return render(request, 'item/items.html',{'item_list':item_list})

def regist(request):
    if request.method == 'POST':
        regist_form = ItemForm(request.POST)
        if regist_form.is_valid():
            item_form = regist_form.save(request.user)
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