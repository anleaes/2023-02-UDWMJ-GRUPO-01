from django.urls import path
from . import views

app_name = 'tipodeprofissional'

urlpatterns = [
    path('', views.list_tipodeprofissional, name='list_tipodeprofissional'),
    path('adicionar/', views.add_tipodeprofissional, name='add_tipodeprofissional'),
    path('editar/<int:id_tipodeprofissional>/', views.edit_tipodeprofissional, name='edit_tipodeprofissional'),
    path('excluir/<int:id_tipodeprofissional>/', views.delete_tipodeprofissional, name='delete_tipodeprofissional'),
]