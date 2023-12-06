from django.urls import path
from . import views

app_name = 'atendimento'

urlpatterns = [
    path('', views.list_atendimento, name='list_atendimento'),
    path('adicionar/<int:id_client>/', views.add_order, name='add_atendimento'),
    path('excluir/<int:id_atendimento/', views.delete_order, name='delete_atendimento'),
    path('excluir-material/<int:id_materiais_atendimento>/', views.delete_materiais_atendimento, name='delete_materiais_atendimento'),
    path('adicionar-material/<int:id_atendimento>/', views.add_materiais_atendimento, name='add_materiais_atendimento'),
    #adcionar/profissional
    #adicionar/servicos
    path('editar-status/<int:id_atendimento>/', views.edit_atendimento_status, name='edit_atendimento_status'),
]