from django.contrib import admin
from .models import Category, Store, Item

# Register your models here.
admin.site.site_header ='OIMS - ADMIN'

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
class StoreAdmin(admin.ModelAdmin):
    list_display = ('name', 'department', 'building')
    list_filter = ['department']
    
class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'store', 'quantity', 'price')
    list_filter = ['category']


admin.site.register(Category, CategoryAdmin)
admin.site.register(Store, StoreAdmin)
admin.site.register(Item, ItemAdmin)