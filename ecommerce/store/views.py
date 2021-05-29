from django.shortcuts import render
from django.views.generic import ListView
from .models import Item


class HomePageView(ListView):
    model = Item
    template_name = 'store/home.html'