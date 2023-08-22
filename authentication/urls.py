from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('profile/', views.profile, name='profile'),
    path('profile/', views.profile_update, name='profile-update'),
    path('logout/', views.logout_view, name='logout'),
]
