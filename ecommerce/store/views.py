from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Item, Employee, Sale
import json

class HomePageView(ListView):
    model = Item
    template_name = 'store/home.html'

class ItemDetailView(DetailView):
    model = Item
    template_name = 'store/item_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        employee = list(Employee.objects.values_list('name'))
        context["employee"] = json.dumps(employee)
        return context
    