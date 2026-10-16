from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add/', views.add_item, name='add_item'),
    path('list/', views.inventory_list, name='inventory_list'),
    path('summary/', views.stock_summary, name='stock_summary'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('delete/<int:item_id>/', views.delete_item, name='delete_item'),  
]