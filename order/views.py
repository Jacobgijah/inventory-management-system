from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def add_order(request):
    return render(request, 'order/order-add.html')

@login_required
def manage_order(request):
    return render(request, 'order/order-manage.html')