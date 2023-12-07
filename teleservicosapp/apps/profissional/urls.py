from django.urls import path
from . import views

app_name = 'profissional'

urlpatterns = [
    path('', views.list_profissional, name='list_profissional'),
    path('adicionar/', views.add_profissional, name='add_profissional'),
    path('editar/<int:id_profissional>/', views.edit_profissional, name='edit_profissional'),
    path('excluir/<int:id_profissional>/', views.delete_profissional, name='delete_profissional'),
]