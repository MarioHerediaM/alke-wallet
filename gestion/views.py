from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Cliente

# Create your views here.
class ClienteListView(ListView):
    model = Cliente
    template_name = 'gestion/cliente_list.html'

class ClienteCreateView(CreateView):
    model = Cliente
    fields = ['nombre', 'email', 'telefono', 'direccion']
    template_name = 'gestion/cliente_form.html'
    success_url = reverse_lazy('cliente-list')

class ClienteUpdateView(UpdateView):
    model = Cliente
    fields = ['nombre', 'email', 'telefono', 'direccion']
    template_name = 'gestion/cliente_form.html'
    success_url = reverse_lazy('cliente-list')

class ClienteDeleteView(DeleteView):
    model = Cliente
    template_name = 'gestion/cliente_confirm_delete.html'
    success_url = reverse_lazy('cliente-list')