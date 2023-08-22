from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Item, Store, Brand, Attribute
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.paginator import Paginator

@login_required
def index(request):
    total_brands = Brand.objects.count()
    total_items = Item.objects.count()
    total_users = User.objects.count()
    
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
        "brand_percentage_change": brand_percentage_change,
        "item_percentage_change": item_percentage_change,
        "user_percentage_change": user_percentage_change,
    }
    return render(request, 'dashboard/index.html', context)

@login_required
def staff_index(request):
    return render(request, 'dashboard/staff-index.html')

@login_required
def view_items(request):
    items = Item.objects.all() # using ORM
    
    context = {
        'items': items,
    }
    return render(request, 'dashboard/view-items.html', context)

@login_required
def view_stores(request):
    stores = Store.objects.all()
    
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
            messages.error(request, "A brand with the same details already exists.")
            return render(request, "dashboard/add-brand.html", context)
        
        Brand.objects.create(name=brand, description=description)
        messages.success(request, "Brand submitted successfully")
        return redirect("add-brand")

@login_required
def delete_brand(request, id):
    brand = Brand.objects.get(pk=id)
    brand.delete()
    messages.success(request, "Brand removed successfully")
    return redirect('add-brand')

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
        messages.success(request, "Brand updated successfully")
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
        brand_name = request.POST['brand']

        # Check for data redundancy before creating the attribute entry
        existing_attribute = Attribute.objects.filter(
                        model_name=model_name, generation=generation,
                        manufacture_year=manufactured_date, attribute_type=attribute_name
                        ).exists()

        if existing_attribute:
            messages.error(request, "An attribute with the same details already exists.")
            return render(request, "dashboard/add-attribute.html", context)
        
        # Retrieve the Brand instance using the brand name
        brand_instance = Brand.objects.get(name=brand_name)

        new_attribute = Attribute.objects.create(
            attribute_type=attribute_name,
            model_name=model_name,
            generation=generation,
            manufacture_year=manufactured_date,
            brand=brand_instance
        )
        messages.success(request, "Attribute submitted successfully")
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
        new_brand_name = request.POST['brand']
        
        # Retrieve the Brand instance using the new_brand_instance
        new_brand_instance = Brand.objects.get(name=new_brand_name)
        
        attribute.attribute_type = new_attribute_name
        attribute.model_name = new_model_name
        attribute.generation = new_generation
        attribute.manufacture_year = new_manufactured_date
        attribute.brand = new_brand_instance
        attribute.save()
        messages.success(request, "Attribute updated successfully")
        return redirect("manage-attribute") 
    

@login_required
def delete_attribute(request, id):
    attribute = Attribute.objects.get(pk=id)
    attribute.delete()
    messages.success(request, "Attribute removed successfully")
    return redirect('manage-attribute')

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
