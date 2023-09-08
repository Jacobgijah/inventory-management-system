from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Item, Store, Brand, Attribute
from order.models import Order
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Count

@login_required
def index(request):
    total_brands = Brand.objects.count()
    total_items = Item.objects.count()
    total_users = User.objects.count()
    total_orders = Order.objects.count()
    
    orders = Order.objects.all()
    
    # calculate the percentage increase or decrease in the 
    # total number of brands, items users compared to a previous value
    # set the previous values to one
    previous_total_brands = 1 
    previous_total_items = 1
    previous_total_users = 1
    
    brand_percentage_change = ((total_brands - previous_total_brands) / previous_total_brands) * 100
    item_percentage_change = ((total_items - previous_total_items) / previous_total_items) * 100
    user_percentage_change = ((total_users - previous_total_users) / previous_total_users) * 100 
    
    
    context = {
        "total_brands": total_brands,
        "total_items": total_items,
        "total_users": total_users,
        "total_orders": total_orders,
        "orders": orders,
        "brand_percentage_change": brand_percentage_change,
        "item_percentage_change": item_percentage_change,
        "user_percentage_change": user_percentage_change,
    }
    return render(request, 'dashboard/index.html', context)

@login_required
def staff_index(request):
    total_brands = Brand.objects.count()
    total_items = Item.objects.count()
    
    context = {
        "total_brands": total_brands,
        "total_items": total_items,
    }
    
    return render(request, 'dashboard/staff-index.html', context)

@login_required
def view_items(request):
    items = Item.objects.all() # using ORM
    paginator = Paginator(items, 5)
    page_no = request.GET.get("page")
    page_obj = Paginator.get_page(paginator, page_no)
    context = {
        'items': items,
        "page_obj": page_obj,
    }
    return render(request, 'dashboard/view-items.html', context)

@login_required
def history_items(request):
    items = Item.objects.all()
    orders = Order.objects.all()
    paginator = Paginator(items, 5)
    page_no = request.GET.get("page")
    page_obj = Paginator.get_page(paginator, page_no)
    context = {
        'items': items,
        'orders': orders,
        "page_obj": page_obj,
    }
    return render(request, 'dashboard/history-items.html', context)
    
    
@login_required
def view_stores(request):
    stores = Store.objects.annotate(item_count=Count('item')) 
    context = {
        'stores': stores,
    }
    return render(request, 'dashboard/view-stores.html', context)

@login_required
def add_brand(request):
    brands = Brand.objects.all()
    paginator = Paginator(brands, 5)
    page_no = request.GET.get("page")
    page_obj = Paginator.get_page(paginator, page_no)
    context = {
        "brands": brands,
        "page_obj": page_obj,
    }
    
    if request.method == 'GET':    
        return render(request, 'dashboard/add-brand.html', context)

    if request.method == 'POST':
        brand = request.POST['brand']
        description = request.POST['description']
    
        # Check for data redundancy before creating the loan entry
        existing_brand = Brand.objects.filter(name=brand).exists()
        
        if existing_brand:
            messages.error(request, f'{brand} brand with the same details already exists.')
            return render(request, "dashboard/add-brand.html", context)
        
        Brand.objects.create(name=brand, description=description)
        messages.success(request, f'{brand} brand submitted successfully.')
        return redirect("add-brand")

@login_required
def delete_brand(request, id):
    brand = Brand.objects.get(pk=id)
    if request.method == 'POST':
        brand.delete()
        messages.success(request, f"{brand} brand removed successfully")
        return redirect('add-brand')
    return render(request, 'dashboard/delete-brand.html')

@login_required
def edit_brand(request, id):
    brand = Brand.objects.get(pk=id)
    context = {
        'brand': brand,
        'values': brand,
    }
    
    if request.method == 'GET':    
        return render(request, 'dashboard/edit-brand.html', context)

    if request.method == 'POST':
        new_brand_name = request.POST['brand']  # Rename to new_brand_name
        new_description = request.POST['description'] # Rename to new_description
        
        brand.name = new_brand_name  # Assign new_brand_name to brand.name
        brand.description = new_description # Assign new_description to brand.description
        brand.save()
        messages.success(request, f"{new_brand_name} brand updated successfully")
        return redirect("manage-brand")  # Pass id to the URL

@login_required
def manage_brand(request):
    brands = Brand.objects.all()
    paginator = Paginator(brands, 5)
    page_no = request.GET.get("page")
    page_obj = Paginator.get_page(paginator, page_no)
    context = {
        "brands": brands,
        "page_obj": page_obj,
    }

    if request.method == 'GET':    
        return render(request, 'dashboard/manage-brand.html', context)
    
@login_required
def add_attribute(request):
    attributes = Attribute.objects.all()
    brands = Brand.objects.all()
    paginator = Paginator(attributes, 5)
    page_no = request.GET.get("page")
    page_obj = Paginator.get_page(paginator, page_no)
    context = {
        "attributes": attributes,
        "brands": brands,
        "page_obj": page_obj,
    }
    
    if request.method == 'GET':    
        return render(request, 'dashboard/add-attribute.html', context)

    if request.method == 'POST':
        attribute_name = request.POST['attribute']
        model_name = request.POST['model_name']
        generation = request.POST['generation']
        manufactured_date = request.POST['manufactured_date']

        # Check for data redundancy before creating the attribute entry
        existing_attribute = Attribute.objects.filter(
                        model_name=model_name, generation=generation,
                        manufacture_year=manufactured_date, attribute_type=attribute_name
                        ).exists()

        if existing_attribute:
            messages.error(request, f"{model_name} attribute with the same details already exists.")
            return render(request, "dashboard/add-attribute.html", context)
        

        new_attribute = Attribute.objects.create(
            attribute_type=attribute_name,
            model_name=model_name,
            generation=generation,
            manufacture_year=manufactured_date,
        )
        messages.success(request, f"{model_name} attribute submitted successfully")
        return redirect("add-attribute")

@login_required
def edit_attribute(request, id):
    attribute = Attribute.objects.get(pk=id)
    brands = Brand.objects.all()
    context = {
        'attribute': attribute,
        "brands": brands,
        'values': attribute,
    }
    
    if request.method == 'GET':    
        return render(request, 'dashboard/edit-attribute.html', context)
    
    if request.method == 'POST':
        new_attribute_name = request.POST['attribute']
        new_model_name = request.POST['model_name']
        new_generation = request.POST['generation']
        new_manufactured_date = request.POST['manufactured_date']
        
        attribute.attribute_type = new_attribute_name
        attribute.model_name = new_model_name
        attribute.generation = new_generation
        attribute.manufacture_year = new_manufactured_date
        attribute.save()
        messages.success(request, f"{new_model_name} attribute updated successfully")
        return redirect("manage-attribute") 
    

@login_required
def delete_attribute(request, id):
    attribute = Attribute.objects.get(pk=id)
    if request.method == 'POST':
        attribute.delete()
        messages.success(request, f" The ``{attribute}`` attribute removed successfully")
        return redirect('manage-attribute')
    return render(request, 'dashboard/delete-attribute.html')

@login_required
def manage_attribute(request):
    attributes = Attribute.objects.all()
    paginator = Paginator(attributes, 5)
    page_no = request.GET.get("page")
    page_obj = Paginator.get_page(paginator, page_no)
    context = {
        "attributes": attributes,
        "page_obj": page_obj,
    }

    if request.method == 'GET':    
        return render(request, 'dashboard/manage-attribute.html', context)
    
@login_required
def add_items(request):
    items = Item.objects.all()
    brands = Brand.objects.all()
    stores = Store.objects.all()
    models = Attribute.objects.all()
    paginator = Paginator(items, 5)
    page_no = request.GET.get("page")
    page_obj = Paginator.get_page(paginator, page_no)
    context = {
        "items": items,
        "brands": brands,
        "stores": stores,
        "models": models,
        "categories": Item.CATEGORY,  
        "page_obj": page_obj,
    }
    
    if request.method == 'GET':    
        return render(request, 'dashboard/add-items.html', context)
    
    if request.method == 'POST':
        name = request.POST['name']
        brand_name = request.POST['brand']  # Retrieve brand name from POST data
        model_name = request.POST['model_name']
        category = request.POST.get("category")
        store_name = request.POST['store']  # Retrieve store name from POST data
        serial_no = request.POST['serial_no']
        imei = request.POST['imei']
        quantity = request.POST['quantity']
        price = request.POST['price']
        warranty = request.POST['warranty']
        remarks = request.POST['remarks']
        description = request.POST['description']

    # Check for data redundancy before creating the attribute entry
    existing_item = Item.objects.filter(
                        name=name, category=category,
                        serial_no=serial_no, imei=imei,
                    ).exists()

    if existing_item:
        messages.error(request, f"The item `{name}` with the same details already exists.")
        return render(request, "dashboard/add-items.html", context)
    
    # Retrieve the Brand, Attribute & Store instances using the brand_name, model_name and store_name
    brand_instance = Brand.objects.get(name=brand_name)
    store_instance = Store.objects.get(name=store_name)
    model_instance = Attribute.objects.get(model_name=model_name)

    new_item = Item.objects.create(
        created_by=request.user,
        name=name, brand=brand_instance, model_name=model_instance, category=category, store=store_instance, serial_no=serial_no,
        imei=imei, quantity=quantity, price=price, warranty=warranty, remarks=remarks,
        description=description
    )
    messages.success(request, f"The `{name}` item submitted successfully")
    return redirect("add-items")

@login_required
def manage_items(request):
    items = Item.objects.all()
    brands = Brand.objects.all()
    stores = Store.objects.all()
    models = Attribute.objects.all()
    paginator = Paginator(items, 5)
    page_no = request.GET.get("page")
    page_obj = Paginator.get_page(paginator, page_no)
    context = {
        "items": items,
        "brands": brands,
        "stores": stores,
        "models": models,
        "categories": Item.CATEGORY,  
        "page_obj": page_obj,
    }
    
    if request.method == 'GET':    
        return render(request, 'dashboard/manage-items.html', context)

@login_required
def delete_items(request, id):
    item = Item.objects.get(pk=id)
    if request.method == 'POST':
        item.delete()
        messages.success(request, f"The ``{item}`` item removed successfully")
        return redirect('manage-items')
    return render(request, 'dashboard/delete-items.html')
 
@login_required   
def edit_items(request, id):
    item = Item.objects.get(pk=id)
    brands = Brand.objects.all()
    models = Attribute.objects.all()
    stores = Store.objects.all()
    context = {
        'item': item,
        'brands': brands,
        'models': models,
        'stores': stores,
        'categories': Item.CATEGORY,
        'values': item,
    }
    
    if request.method == 'GET':    
        return render(request, 'dashboard/edit-items.html', context)
    
    if request.method == 'POST':
        new_name = request.POST['name']
        new_brand_name = request.POST['brand']  # Retrieve brand name from POST data
        new_model_name = request.POST['model_name']
        new_category = request.POST.get("category")
        new_store_name = request.POST['store']  # Retrieve store name from POST data
        new_serial_no = request.POST['serial_no']
        new_imei = request.POST['imei']
        new_quantity = request.POST['quantity']
        new_price = request.POST['price']
        new_warranty = request.POST['warranty']
        new_remarks = request.POST['remarks']
        new_description = request.POST['description']
        
        # Retrieve the Brand, Attribute & Store instances using the brand_name, model_name and store_name
        new_brand_instance = Brand.objects.get(name=new_brand_name)
        new_store_instance = Store.objects.get(name=new_store_name)
        new_model_instance = Attribute.objects.get(model_name=new_model_name)

        item.name = new_name
        item.brand = new_brand_instance
        item.model_name = new_model_instance
        item.serial_no = new_serial_no
        item.imei = new_imei
        item.category = new_category
        item.store = new_store_instance
        item.description = new_description
        item.quantity = new_quantity
        item.warranty = new_warranty
        item.price = new_price
        item.remarks = new_remarks
        item.save()
        messages.success(request, f"The {new_name} item updated successfully")
        return redirect("manage-items")

@login_required
def detail_items(request, id):
    item = Item.objects.get(pk=id)
    stores = Store.objects.all()
    context = {
        'item': item,
        'stores': stores,
        'values': item,
    }
    
    if request.method == 'GET':    
        return render(request, 'dashboard/detail-items.html', context)

@login_required
def receive_items(request, id):
    item = get_object_or_404(Item, pk=id)
    context = {
        'item': item,
    }
    
    if request.method == 'GET':    
        return render(request, 'dashboard/receive-items.html', context)

    if request.method == 'POST':
        receive_quantity = request.POST['quantity']
        
        instance_quantity = int(receive_quantity)
        
        item.receive_quantity = instance_quantity
        item.quantity += item.receive_quantity
        item.save()
        messages.success(request, f"Successfully added: {instance_quantity} quantity of item {item.name}.")
        return redirect("detail-items", id=item.id)
    
@login_required
def reorder_level(request, id):
    item = get_object_or_404(Item, pk=id)
    context = {
        'item': item,
    }
    
    if request.method == 'GET':    
        return render(request, 'dashboard/reorder-level.html', context)

    if request.method == 'POST':
        reorder_level = request.POST['quantity']
        
        instance_reorder_level = int(reorder_level)
        
        item.reorder_level = instance_reorder_level
        item.save()
        messages.success(request, f"Successfully added: {instance_reorder_level} reorder level of item {item.name}.")
        return redirect("detail-items", id=item.id)
    

