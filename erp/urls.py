from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('inventory/', views.inventory, name = 'inventory'),
    path('product-create/', views.product_create, name = 'product_create'),
    path('product-list/', views.product_list, name ='product_list'),
    path('inbound-create/', views.inbound_create, name='inbound_create'),
    path('outbound-create/', views.outbound_create, name='outbound_create'),
    path('delete-all/', views.delete_all, name ='delete_all')
]