from django.contrib import admin
from .models import Item, Employee, Sale, UpdatedItemPrice

admin.site.register(Item)
admin.site.register(Employee)
admin.site.register(Sale)


@admin.register(UpdatedItemPrice)
class UpdatedItemPriceAdmin(admin.ModelAdmin):
    list_display = ('item', 'updated_price', 'update_date')
    list_filter = ['item']