from django.shortcuts import render
from annoying.decorators import render_to
from .models import Item

@render_to('store/home.html')
def home_view(request):
    items = Item.objects.all()
    return {'items': items}
