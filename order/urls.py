from django.urls import path
from . import views

urlpatterns = [
    path('order-add/', views.add_order, name='order-add'),
    path('order-manage/', views.manage_order, name='order-manage'),
    path("order-delete/<int:id>", views.delete_order, name="order-delete"),
    path("order-edit/<int:id>", views.edit_order, name="order-edit"),
    path("order-detail/<int:id>", views.detail_order, name="order-detail"),
    path('order-request/', views.request_order, name='order-request'),
    path('update-status/', views.update_order_status, name='update-order-status'),
    
]