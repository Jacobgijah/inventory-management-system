from django.contrib import admin
from .models import Product, Order

# Register your models here.
admin.site.site_header ='OIMS - ADMIN'

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'quantity')
    list_filter = ['category']

class OrderAdmin(admin.ModelAdmin):
    list_display = ('staff', 'product', 'order_quantity', 'order_date')
    list_filter = ['product']

admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)