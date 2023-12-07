from django.contrib import admin
from django.urls import path
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls', namespace='core')),
    path('tiposdeprofissional/', include('tiposdeprofissional.urls', namespace='tiposdeprofissional')),
    path('clientes/', include('clients.urls', namespace='clients')),
    path('materiais', include('materiais.urls', namespace='materiais')),
    path('profissionais/', include('profissionais.urls', namespace='profissionais')),
    path('contas/', include('accounts.urls', namespace='accounts')),
    path('atendimentos/', include('atendimentos.urls', namespace='atendimentos')),
    path('servicos/', include('servicos.urls', namespace='servicos')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)