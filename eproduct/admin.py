from django.contrib import admin
from .models import Item


class ItemAdmin(admin.ModelAdmin):
    list_display = ('fruit_name', 'price', 'stock')

admin.site.register(Item, ItemAdmin)


