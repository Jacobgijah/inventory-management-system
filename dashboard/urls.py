from django.urls import path
from . import views

urlpatterns = [
    path('index', views.index, name='index'),
    path('view-items', views.view_items, name='view-items'),
    path('view-stores', views.view_stores, name='view-stores'),

]