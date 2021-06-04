from django import forms
from django.forms import fields
from .models import Sale, Employee

class SalesForms(forms.ModelForm):
  
    class Meta:
        model = Sale
        fields = ['item', 'employee', 'qty']
