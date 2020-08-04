from django.http import HttpResponse
from django.shortcuts import render
from. models import Item


def index(request):
    a = Item.objects.all
    return render(request, 'index.html',{'pro':a})
