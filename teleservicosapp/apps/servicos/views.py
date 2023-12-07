from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from .forms import ServicosForm, ServicosItemForm
from .models import Servicos , ServicosItem, Profissionais, Client

# Create your views here.

def add_servicos(request, id_client):
    template_name = 'servicos/add_servicos.html'
    context = {}
    if request.method == 'POST':
        form = ServicosForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.client = Client.objects.get(id=id_client)
            f.save()
            form.save_m2m()
            return redirect('servicos:list_servicos')
    form = ServicosForm()
    context['form'] = form
    return render(request, template_name, context)

def list_servicos(request):
    template_name = 'servicos/list_servicos.html'
    orders = Servicos.objects.filter()
    order_items = ServicosItem.objects.filter()
    products = Profissionais.objects.filter()
    clients = Client.objects.filter()
    context = {
        'orders': orders,
        'order_items': order_items,
        'products': products,
        'clients': clients
    }
    return render(request, template_name, context)

def delete_servicos(request, id_order):
    order = Servicos.objects.get(id=id_order)
    order.delete()
    return redirect('servicos:list_servicos')

def add_servicos_item(request, id_order):
    template_name = 'servicos/add_servico_item.html'
    context = {}
    if request.method == 'POST':
        form = ServicosItemForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.order = Servicos.objects.get(id=id_order)
            f.save()
            form.save_m2m()
            return redirect('servicos:list_servicos')
    form = ServicosItemForm()
    context['form'] = form
    return render(request, template_name, context)

def delete_servicos_item(request, id_order_item):
    servicosItem = ServicosItem.objects.get(id=id_order_item)
    servicosItem.delete()
    return redirect('servicos:list_servicos')

def edit_servicos_status(request, id_order):
    template_name = 'servicos/edit_servico_status.html'
    context ={}
    order = get_object_or_404(Servicos, id=id_order)
    if request.method == 'POST':
        form = ServicosForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('servicos:list_servicos')
    form = ServicosForm(instance=order)
    context['form'] = form
    return render(request, template_name, context)