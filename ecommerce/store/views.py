from django.shortcuts import redirect, render
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import View
from .models import Item, Sale, UpdatedItemPrice
from .forms import SalesForms
from django.contrib import messages


class HomePageView(ListView):
    model = Item
    template_name = 'store/home.html'
    paginate_by = 9

class ConfirmSaleView(View):

    def get(self, request, *args, **kwargs):
        context = {}
        item = Item.objects.get(slug=self.kwargs.get('slug'))
        context["item"] = item
        context["form"] = SalesForms()
        return render(request,'store/confirm_sale.html', context=context )

    def post(self, request, *args, **kwargs):
        form = SalesForms(self.request.POST)     
        item = Item.objects.get(slug=self.kwargs.get('slug'))
     
        if form.is_valid(): 
            employee = form.cleaned_data['employee'] 
            qty = form.cleaned_data['qty'] 
            sale = Sale(item=item, employee=employee, qty=qty)     
            sale.save()
            messages.success(request, f'Спасибо за покупку!')
            return redirect('home')
        else:
            messages.warning(request, f'Что-то пошло не так!')
            return self.get(request, *args, **kwargs)
            

class SaleList(LoginRequiredMixin, ListView):
    model = Sale
    template_name = 'store/sale_list.html'
    paginate_by = 5
    

class UpdatedPriceList(LoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):
        item = Item.objects.get(slug=self.kwargs.get('slug'))
        updated_price = UpdatedItemPrice.objects.filter(item=item)
        return render(request, 'store/updated_price_list.html', {'updated_price': updated_price, 'item': item })
