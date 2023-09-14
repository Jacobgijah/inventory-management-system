from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('staff-index/', views.staff_index, name='staff-index'),
    path('add-items/', views.add_items, name='add-items'),
    path('manage-items/', views.manage_items, name='manage-items'),
    path('view-items/', views.view_items, name='view-items'),
    path('history-items/', views.history_items, name='history-items'),
    path("report-items/", views.report_items, name="report-items"),
    path("edit-items/<int:id>", views.edit_items, name="edit-items"),
    path('delete-items/<int:id>', views.delete_items, name='delete-items'),
    path('detail-items/<int:id>', views.detail_items, name='detail-items'),
    path('receive-items/<int:id>', views.receive_items, name='receive-items'),
    path('reorder-level/<int:id>', views.reorder_level, name='reorder-level'),
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