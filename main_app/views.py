from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Item


def home(request):
    return render(request, 'home.html')


def items_index(request):
    items = Item.objects.all()
    return render(request, 'items/index.html', { 'items': items })


class ItemCreate(CreateView):
    model = Item
    fields = '__all__'
    success_url = '/items'
