from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from .forms import TipodeprofissionalForm
from .models import Tipodeprofissional

# Create your views here.

def add_tipodeprofissional(request):
    template_name = 'tipodeprofissional/add_tipodeprofissional.html'
    context = {}
    if request.method == 'POST':
        form = TipodeprofissionalForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            form.save_m2m()
            return redirect('tipodeprofissional:list_tipodeprofissional')
    form = TipodeprofissionalForm()
    context['form'] = form
    return render(request, template_name, context)

def list_tipodeprofissional(request):
    template_name = 'tipodeprofissional/list_tipodeprofissional.html'
    tipodeprofissional = Tipodeprofissional.objects.filter()
    context = {
        'tipodeprofissional': tipodeprofissional
    }
    return render(request, template_name, context)

def edit_tipodeprofissional(request, id_tipodeprofissional):
    template_name = 'tipodeprofissional/add_tipodeprofissional.html'
    context ={}
    tipodeprofissional = get_object_or_404(Tipodeprofissional, id=id_tipodeprofissional)
    if request.method == 'POST':
        form = TipodeprofissionalForm(request.POST, instance=tipodeprofissional)
        if form.is_valid():
            form.save()
            return redirect('tipodeprofissional:list_tipodeprofissional')
    form = TipodeprofissionalForm(instance=tipodeprofissional)
    context['form'] = form
    return render(request, template_name, context)

def delete_tipodeprofissional(request, id_tipodeprofissional):
    tipodeprofissional = Tipodeprofissional.objects.get(id=id_tipodeprofissional)
    tipodeprofissional.delete()
    return redirect('tipodeprofissional:list_tipodeprofissional')