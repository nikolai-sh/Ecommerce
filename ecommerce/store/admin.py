from django.contrib import admin
from .models import Item, Employee, Sale, UpdatedItemPrice


admin.site.register(Employee)
admin.site.register(Sale)


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        update_fields = []
        # True if something changed in model
        # Note that change is False at the very first time
        if change: 
            #check what field was changed and add it to update_fields
            for field in form.fields:
                if form.initial[field] != form.cleaned_data[field]:
                    update_fields.append(field)
                
        obj.save(update_fields=update_fields)
        

@admin.register(UpdatedItemPrice)
class UpdatedItemPriceAdmin(admin.ModelAdmin):
    list_display = ('item', 'updated_price', 'update_date')
    list_filter = ['item']