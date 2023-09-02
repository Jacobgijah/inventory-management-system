from django.contrib import admin
from .models import Brand, Attribute, Store, Item

# Register your models here.
admin.site.site_header ='OIMS - ADMIN'

class BrandAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    
class AttributeAdmin(admin.ModelAdmin):
    list_display = ('model_name', 'generation', 'attribute_type', 'manufacture_year')
    list_filter = ['attribute_type']

class StoreAdmin(admin.ModelAdmin):
    list_display = ('name', 'building', 'room')
    list_filter = ['building']
        
class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'brand', 'model_name', 'category', 'store', 'quantity', 
                    'reorder_level', 'warranty', 'registered_date', 'last_updated', 'price')
    list_filter = ['category', 'brand', 'store', 'model_name']


admin.site.register(Brand, BrandAdmin)
admin.site.register(Attribute, AttributeAdmin)
admin.site.register(Store, StoreAdmin)
admin.site.register(Item, ItemAdmin)