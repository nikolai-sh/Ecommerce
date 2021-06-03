from django.http import request
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Item, Employee, Sale


class HomePageView(ListView):
    model = Item
    template_name = 'store/home.html'

class ItemDetailView(DetailView):
    model = Item
    template_name = 'store/item_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        employee = Employee.objects.all()
        context["employee"] = employee
        return context
    
    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            
            print(employee=request.POST.get(form.option.value))

            