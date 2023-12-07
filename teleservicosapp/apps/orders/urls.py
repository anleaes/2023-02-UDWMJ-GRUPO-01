from django.urls import path
from . import views

app_name = 'orders'

urlpatterns = [
    path('', views.list_orders, name='list_orders'),
    path('adicionar/<int:id_client>/', views.add_order, name='add_order'),
    path('excluir/<int:id_order>/', views.delete_order, name='delete_order'),
    path('excluir-item/<int:id_order_item>/', views.delete_order_item, name='delete_order_item'),
    path('adicionar-item/<int:id_order>/', views.add_order_item, name='add_order_item'),
    path('editar-status/<int:id_order>/', views.edit_order_status, name='edit_order_status'),
]