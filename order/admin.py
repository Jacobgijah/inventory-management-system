from django.contrib import admin
from .models import Order 

# Register your models here.
admin.site.site_header ='OIMS - ADMIN'

class OrderAdmin(admin.ModelAdmin):
    list_display = ('item', 'quantity', 'issued_date', 'created_by', 'status')
    list_filter = ['item', 'status', 'created_by']

admin.site.register(Order, OrderAdmin)