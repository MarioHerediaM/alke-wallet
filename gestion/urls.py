from django.urls import path
from .views import ClienteCreateView, ClienteDeleteView, ClienteListView, ClienteUpdateView

urlpatterns = [
    path('clientes/', ClienteListView.as_view(), name='cliente-list'),
    path('clientes/nuevo/', ClienteCreateView.as_view(), name = 'cliente-create'),
    path('clientes/<int:pk>/editar/', ClienteUpdateView.as_view(), name='cliente-update'),
    path('clientes/<int:pk>/eliminar/', ClienteDeleteView.as_view(), name='cliente-delete'),
]