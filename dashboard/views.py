from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def index(request):
    return render(request, 'dashboard/index.html')

@login_required(login_url='login')
def view_items(request):
    return render(request, 'dashboard/view-items.html')

@login_required(login_url='login')
def view_stores(request):
    return render(request, 'dashboard/view-stores.html')