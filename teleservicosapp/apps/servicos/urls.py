from django.urls import path
from . import views

app_name = 'servicos'

urlpatterns = [
    path('', views.list_servicos, name='list_servicos'),
    path('adicionar/<int:id_client>/', views.add_servicos, name='add_servicos'),
    path('excluir/<int:id_servicos>/', views.delete_servicos, name='delete_servicos'),
    path('excluir-item/<int:id_servicos_item>/', views.delete_servicos_item, name='delete_servicos_item'),
    path('adicionar-item/<int:id_servicos>/', views.add_servicos_item, name='add_servicos_item'),
    path('editar-status/<int:id_servicos>/', views.edit_servicos_status, name='edit_servicos_status'),
]