from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from .forms import ClientForm
from .models import Client, Socialnetwork, ClientSocialnetwork

# Create your views here.
def add_client(request):
    template_name = 'clients/add_client.html'
    context = {}
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            form.save_m2m()
            return redirect('clients:list_clients')
    form = ClientForm()
    context['form'] = form
    return render(request, template_name, context)

def list_clients(request):
    template_name = 'clients/list_clients.html'
    client_socialnetworks = ClientSocialnetwork.objects.filter()
    socialnetworks = Socialnetwork.objects.filter()
    clients = Client.objects.filter()
    context = {
        'clients': clients,
        'socialnetworks': socialnetworks,
        'client_socialnetworks': client_socialnetworks
    }
    return render(request, template_name, context)

def edit_client(request, id_client):
    template_name = 'clients/add_client.html'
    context ={}
    client = get_object_or_404(Client, id=id_client)
    if request.method == 'POST':
        form = ClientForm(request.POST, instance=client)
        if form.is_valid():
            form.save()
            return redirect('clients:list_clients')
    form = ClientForm(instance=client)
    context['form'] = form
    return render(request, template_name, context)

def delete_client(request, id_client):
    client = Client.objects.get(id=id_client)
    client.delete()
    return redirect('clients:list_clients')
