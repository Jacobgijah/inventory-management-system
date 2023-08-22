from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('staff-index/', views.staff_index, name='staff-index'),
    path('view-items/', views.view_items, name='view-items'),
    path('view-stores/', views.view_stores, name='view-stores'),
    path('add-brand/', views.add_brand, name='add-brand'),
    path('manage-brand/', views.manage_brand, name='manage-brand'),
    path("delete-brand/<int:id>", views.delete_brand, name="delete-brand"),
    path("edit-brand/<int:id>", views.edit_brand, name="edit-brand"),
    path("add-attribute/", views.add_attribute, name="add-attribute"),
    path("delete-attribute/<int:id>", views.delete_attribute, name="delete-attribute"),
    path("edit-attribute/<int:id>", views.edit_attribute, name="edit-attribute"),
    path('manage-attribute/', views.manage_attribute, name='manage-attribute'),
]