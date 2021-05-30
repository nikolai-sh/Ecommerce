from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Item


class HomePageView(ListView):
    model = Item
    template_name = 'store/home.html'

class ItemDetailView(DetailView):
    model = Item
    template_name = 'store/item_detail.html'