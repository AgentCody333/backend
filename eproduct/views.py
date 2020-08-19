from django.http import HttpResponse
from django.shortcuts import render
from. models import Item


def index(request):
    a = Item.objects.all
    return render(request, 'index.html',{'pro':a})


def searchbar(request):
    if request.method == 'GET' :
        search = request.GET.get('search')
        post = Item.objects.all().filter(fruit_name = search)
        return render(request, 'search.html', {'post':post})
