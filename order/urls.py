from django.urls import path
from . import views

urlpatterns = [
    path('order-add/', views.add_order, name='order-add'),
    path('order-manage/', views.manage_order, name='order-manage'),
]