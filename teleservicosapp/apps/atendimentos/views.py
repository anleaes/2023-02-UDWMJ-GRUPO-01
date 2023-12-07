from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect

import atendimentos
from .forms import AtendimentoForm, MateriaisAtendimentoForm
from .models import Atendimentos, MateriaisAtendimentos, Materiais, Client
#import profissional, servico

# Create your views here.
def add_atendimento(request, id_client):
    template_name = 'atendimentos/add_atendimentos.html'
    context = {}
    if request.method == 'POST':
        form = AtendimentoForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.client = Client.objects.get(id=id_client)
            f.save()
            #add profissional,servicos
            form.save_m2m()
            return redirect('atendimentos:list_atendimentos')
    form = AtendimentoForm()
    context['form'] = form
    return render(request, template_name, context)

def list_atendimentos(request):
    template_name = 'atendimentos/list_atendimentos.html'
    atendimento =   Atendimentos.objects.filter()
    materiaisatendimento = MateriaisAtendimentos.objects.filter()
    materiais = Materiais.objects.filter()
    clients = Client.objects.filter()
    #list profissionais, servicos
    context = {
        'atendimento': atendimento,
        'materiaisatendimento': materiaisatendimento,
        'materiais': materiais,
        'clients': clients
    }
    return render(request, template_name, context)

def delete_atendimento(request, id_atendimento):
    atendimento = Atendimentos.objects.get(id=id_atendimento)
    atendimento.delete()
    return redirect('atendimentos:list_atendimentos')

def add_materiais_atendimento(request, id_atendimento):
    template_name = 'atendimento/add_materiais_atendimento.html'
    context = {}
    if request.method == 'POST':
        form = MateriaisAtendimentos(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.atendimento = Atendimentos.objects.get(id=id_atendimento)
            f.save()
            form.save_m2m()
            return redirect('atendimentos:list_atendimentos')
    form = MateriaisAtendimentoForm()
    context['form'] = form
    return render(request, template_name, context)

def delete_materiais_atendimento(request, id_materiais_atendimento):
    materiaisatendimento = MateriaisAtendimentos.objects.get(id=id_materiais_atendimento)
    materiaisatendimento.delete()
    return redirect('atendimentos:list_atendimentos')

def edit_atendimento_status(request, id_atendimento):
    template_name = 'atendimentos/edit_atendimentos_status.html'
    context ={}
    atendimento = get_object_or_404(Atendimentos, id=id_atendimento)
    if request.method == 'POST':
        form = AtendimentoForm(request.POST, instance=atendimento)
        if form.is_valid():
            form.save()
            return redirect('atendimentos:list_atendimentos')
    form = AtendimentoForm(instance=atendimento)
    context['form'] = form
    return render(request, template_name, context)