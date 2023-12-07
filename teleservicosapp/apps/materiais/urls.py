from django.urls import path
from . import views

app_name = 'materiais'

urlpatterns = [
    path('', views.list_materiais, name='list_materiais'),
    path('adicionar/', views.add_materiais, name='add_materiais'),
    path('editar/<int:id_material>/', views.edit_materiais, name='edit_materiais'),
    path('excluir/<int:id_material>/', views.delete_materiais, name='delete_materiais'),
]

