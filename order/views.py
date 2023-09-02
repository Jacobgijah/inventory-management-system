from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Item, Order
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.db import transaction

# Create your views here.

@login_required
def add_order(request):
    orders = Order.objects.all()
    items = Item.objects.all()
    paginator = Paginator(orders, 5)
    page_no = request.GET.get("page")
    page_obj = Paginator.get_page(paginator, page_no)
    context = {
        "orders": orders,
        "items": items,
        "page_obj": page_obj,
    }

    if request.method == 'GET':    
        return render(request, 'order/order-add.html', context)
    
    if request.method == 'POST':
        item_id = request.POST['item']  # Use the item ID instead of the name
        quantity = request.POST['quantity']
        
        # Retrieve the Item instance using the item ID
        item_instance = Item.objects.get(pk=item_id)
        
        Order.objects.create(created_by=request.user, item=item_instance, quantity=quantity)
        messages.success(request, f'{item_instance} order request submitted successfully.')
        return redirect("order-add")

@login_required
def edit_order(request, id):
    order = Order.objects.get(pk=id)
    items = Item.objects.all()
    context = {
        "order": order,
        "items": items,
        'values': order,
    }
    
    if request.method == 'GET':    
        return render(request, 'order/order-edit.html', context)
    
    if request.method == 'POST':
        new_item = request.POST['item']
        new_quantity = request.POST['quantity']
        
        # Retrieve the Item instance using the new_item name
        item_instance = Item.objects.get(name=new_item)
        
        order.item = item_instance
        order.quantity = new_quantity
        order.save()
        messages.success(request, f'{item_instance} order request updated successfully.')
        return redirect("order-manage")
    
@login_required
def delete_order(request, id):
    item = Order.objects.get(pk=id)
    if request.method == 'POST':
        item.delete()
        messages.success(request, f"{item} order request removed successfully")
        return redirect('order-manage')
    return render(request, 'order/order-delete.html')


@login_required
def manage_order(request):
    orders = Order.objects.filter(created_by=request.user)
    paginator = Paginator(orders, 5)
    page_no = request.GET.get("page")
    page_obj = Paginator.get_page(paginator, page_no)
    context = {
        "orders": orders,
        "page_obj": page_obj,
    }
    
    if request.method == 'GET':    
        return render(request, 'order/order-manage.html', context)
    
@login_required
def request_order(request):
    orders = Order.objects.all()
    paginator = Paginator(orders, 5)
    page_no = request.GET.get("page")
    page_obj = Paginator.get_page(paginator, page_no)
    context = {
        "orders": orders,
        "page_obj": page_obj,
    }

    if request.method == 'GET':    
        return render(request, 'order/order-request.html', context)

@login_required
def update_order_status(request):
    if request.method == "POST":
        order_id = request.POST.get("order_id")
        new_status = request.POST.get("new_status")

        try:
            order = Order.objects.get(id=order_id)

            if new_status == "Approved":
                # Check if the requested quantity is less than or equal to the available quantity
                if order.quantity <= order.item.quantity:
                    with transaction.atomic():
                        order.status = new_status
                        order.item.quantity -= order.quantity
                        order.item.save()
                        order.save()
                    return JsonResponse({"success": True})
                else:
                    return JsonResponse({"success": False, "error": "Insufficient quantity available"})

            elif new_status == "Declined":
                order.status = new_status
                order.save()
                return JsonResponse({"success": True})

            else:
                return JsonResponse({"success": False, "error": "Invalid status"})

        except Order.DoesNotExist:
            return JsonResponse({"success": False, "error": "Order not found"})
    else:
        return JsonResponse({"success": False, "error": "Invalid request method"})

@login_required
def detail_order(request, id):
    order = Order.objects.get(pk=id)
    context = {
        'order': order,
        
    }
    
    if request.method == 'GET':    
        return render(request, 'order/order-detail.html', context)
       