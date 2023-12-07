from django.urls import path
from . import views

app_name = 'profissionais'

urlpatterns = [
    path('', views.list_profissionais, name='list_profissionais'),
    path('adicionar/', views.add_profissionais, name='add_profissionais'),
    path('editar/<int:id_profissionais>/', views.edit_profissionais, name='edit_profissionais'),
    path('excluir/<int:id_profissionais>/', views.delete_profissional, name='delete_profissionais'),
]