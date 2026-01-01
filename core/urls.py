from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_dashboard, name='main_dashboard'),                                
    path('client/', views.client_dashboard, name='client_dashboard'),
    path('order/', views.order_dashboard, name='order_dashboard'),      
    path('order/add/<int:client_id>/', views.add_order_for_client, name='add_order_for_client'),
    path('reorder/', views.reorder_dashboard, name='reorder_dashboard'),
    path('inventory/', views.inventory_dashboard, name='inventory_dashboard'),
    path('finance/', views.finance_dashboard, name='finance_dashboard'),
    path('finance/invoice/<int:invoice_id>/', views.view_invoice, name='view_invoice'),
    path('finance/invoice/<int:invoice_id>/pdf/', views.download_invoice_pdf, name='download_invoice_pdf'),
    path('api/clients/', views.client_search_api, name='client_search_api'),
    path('api/material/<int:material_id>/vendors/', views.get_material_vendors, name='material_vendors'),

]