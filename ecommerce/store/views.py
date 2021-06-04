from django.shortcuts import redirect
from django.views.generic import ListView, DetailView
from .models import Item, Employee
from django.views.generic.edit import FormMixin
from .forms import SalesForms


class HomePageView(ListView):
    model = Item
    template_name = 'store/home.html'

class ItemDetailView(FormMixin, DetailView):
    model = Item
    form_class = SalesForms
    template_name = 'store/item_detail.html'


    def get_context_data(self, **kwargs):
        context = super(ItemDetailView, self).get_context_data(**kwargs)
        employee = Employee.objects.all()
        context["employee"] = employee
        context["form"] = SalesForms(initial={'item': self.object})
        return context

    def post(self, request, *args, **kwargs):
        form = self.get_form()     
        if form.is_valid():        
            form.save()
            return redirect('home')

 

 
                    