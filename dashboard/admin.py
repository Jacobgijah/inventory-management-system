from django.contrib import admin
from .models import Brand, Attribute, Store, Item

# Register your models here.
admin.site.site_header ='OIMS - ADMIN'

class BrandAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    
class AttributeAdmin(admin.ModelAdmin):
    list_display = ('brand', 'model_name', 'generation', 'attribute_type', 'manufacture_year')
    list_filter = ['brand']

class StoreAdmin(admin.ModelAdmin):
    list_display = ('name', 'building', 'room')
    list_filter = ['building']
        
class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'brand', 'serial_no', 'imei', 'category', 'store', 'description',
                    'quantity', 'warranty', 'registered_date', 'expiry_date', 'price')
    list_filter = ['category', 'brand', 'store']


admin.site.register(Brand, BrandAdmin)
admin.site.register(Attribute, AttributeAdmin)
admin.site.register(Store, StoreAdmin)
admin.site.register(Item, ItemAdmin)