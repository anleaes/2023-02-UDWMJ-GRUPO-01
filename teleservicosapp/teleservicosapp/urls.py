from django.contrib import admin
from django.urls import path
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls', namespace='core')),
    path('categorias/', include('categories.urls', namespace='categories')),
    path('clientes/', include('clients.urls', namespace='clients')),
    path('pedidos/', include('orders.urls', namespace='orders')),
    path('produtos/', include('products.urls', namespace='products')),
    path('materiais', include('materiais.urls', namespace='materiais')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)