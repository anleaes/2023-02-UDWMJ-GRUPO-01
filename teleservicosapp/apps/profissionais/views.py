from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
import profissionais
from .forms import ProfissionaisForm
from .models import Profissionais

# Create your views here.

@login_required(login_url='/contas/login/')
def add_profissionais(request):
    template_name = 'profissionais/add_profissionais.html'
    context = {}
    if request.method == 'POST':
        form = ProfissionaisForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            form.save_m2m()
            return redirect('profissionais:list_profissionais')
    form = ProfissionaisForm()
    context['form'] = form
    return render(request, template_name, context)

def list_profissionais(request):
    template_name = 'profissionais/list_profissionais.html'
    profissionais = Profissionais.objects.filter()
    context = {
        'profissionais': profissionais,
    }
    return render(request, template_name, context)

@login_required(login_url='/contas/login/')
def edit_profissionais(request, id_profissionais):
    template_name = 'profissionais/add_profissionais.html'
    context ={}
    profissionais = get_object_or_404(Profissionais, id=id_profissionais)
    if request.method == 'POST':
        form = ProfissionaisForm(request.POST, instance=profissionais)
        if form.is_valid():
            form.save()
            return redirect('profissionais:list_profissionais')
    form = ProfissionaisForm(instance=profissionais)
    context['form'] = form
    return render(request, template_name, context)

@login_required(login_url='/contas/login/')
def delete_profissionais(request, id_profissionais):
    profissionais = Profissionais.objects.get(id=id_profissionais)
    profissionais.delete()
    return redirect('profissionais:list_profissionais')