from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from .forms import OrderForm, OrderItemForm
from .models import Order , OrderItem, Product, Client
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='/contas/login/')
def add_order(request, id_client):
    template_name = 'orders/add_order.html'
    context = {}
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.client = Client.objects.get(id=id_client)
            f.save()
            form.save_m2m()
            return redirect('orders:list_orders')
    form = OrderForm()
    context['form'] = form
    return render(request, template_name, context)

@login_required(login_url='/contas/login/')
def list_orders(request):
    template_name = 'orders/list_orders.html'
    orders = Order.objects.filter()
    order_items = OrderItem.objects.filter()
    products = Product.objects.filter()
    clients = Client.objects.filter()
    context = {
        'orders': orders,
        'order_items': order_items,
        'products': products,
        'clients': clients
    }
    return render(request, template_name, context)

@login_required(login_url='/contas/login/')
def delete_order(request, id_order):
    order = Order.objects.get(id=id_order)
    order.delete()
    return redirect('orders:list_orders')

@login_required(login_url='/contas/login/')
def add_order_item(request, id_order):
    template_name = 'orders/add_order_item.html'
    context = {}
    if request.method == 'POST':
        form = OrderItemForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.order = Order.objects.get(id=id_order)
            f.save()
            form.save_m2m()
            return redirect('orders:list_orders')
    form = OrderItemForm()
    context['form'] = form
    return render(request, template_name, context)

@login_required(login_url='/contas/login/')
def delete_order_item(request, id_order_item):
    orderitem = OrderItem.objects.get(id=id_order_item)
    orderitem.delete()
    return redirect('orders:list_orders')

@login_required(login_url='/contas/login/')
def edit_order_status(request, id_order):
    template_name = 'orders/edit_order_status.html'
    context ={}
    order = get_object_or_404(Order, id=id_order)
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('orders:list_orders')
    form = OrderForm(instance=order)
    context['form'] = form
    return render(request, template_name, context)