from django import forms
from .models import Employee

class SalesForms(forms.Form):

    employee = forms.ModelChoiceField( queryset=Employee.objects.all(), required=True)
    qty = forms.DecimalField(initial=1, required=True, min_value=1)
   
    
