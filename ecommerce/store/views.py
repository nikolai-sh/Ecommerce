from django.shortcuts import render
from annoying.decorators import render_to
from django.views.generic import TemplateView
from .models import Item

# @render_to('store/home.html')
# def home_view(request):
#     items = Item.objects.all()
#     return {'items': items}

class HomePageView(TemplateView):
    template_name = 'store/home.html'