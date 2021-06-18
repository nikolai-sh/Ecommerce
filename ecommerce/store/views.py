from django.shortcuts import redirect, render, get_object_or_404
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import View
from .models import Item, Employee, Sale, UpdatedItemPrice
from django.views.generic.edit import FormMixin
from .forms import SalesForms


class HomePageView(ListView):
    model = Item
    template_name = 'store/home.html'
    paginate_by = 9

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

            

 
class SaleList(LoginRequiredMixin, ListView):
    model = Sale
    template_name = 'store/sale_list.html'
    paginate_by = 5

class UpdatedPriceList(LoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):
        item = Item.objects.get(slug=self.kwargs.get('slug'))
        updated_price = UpdatedItemPrice.objects.filter(item=item)
        print(updated_price)
        return render(request, 'store/updated_price_list.html', {'updated_price': updated_price, 'item': item })
