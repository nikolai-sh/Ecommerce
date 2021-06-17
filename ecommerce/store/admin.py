from django.contrib import admin
from .models import Item, Employee, Sale, UpdatedItemPrice

admin.site.register(Item)
admin.site.register(Employee)
admin.site.register(Sale)
admin.site.register(UpdatedItemPrice)
