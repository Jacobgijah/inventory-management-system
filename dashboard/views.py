from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    return render(request, 'dashboard/index.html')

@login_required
def staff_index(request):
    return render(request, 'dashboard/staff-index.html')

@login_required
def view_items(request):
    return render(request, 'dashboard/view-items.html')

@login_required
def view_stores(request):
    return render(request, 'dashboard/view-stores.html')