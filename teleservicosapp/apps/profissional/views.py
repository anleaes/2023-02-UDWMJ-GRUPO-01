from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect

from teleservicosapp.apps import profissional
from .forms import ProfissionalForm
from .models import Profissional

# Create your views here.

def add_profissional(request):
    template_name = 'profissional/add_profissional.html'
    context = {}
    if request.method == 'POST':
        form = ProfissionalForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            form.save_m2m()
            return redirect('profissional:list_profissional')
    form = ProfissionalForm()
    context['form'] = form
    return render(request, template_name, context)

def list_profissional(request):
    template_name = 'profissional/list_profissional.html'
    profissional = Profissional.objects.filter()
    context = {
        'profissional': profissional,
    }
    return render(request, template_name, context)

def edit_profissional(request, id_profissional):
    template_name = 'profissional/add_profissional.html'
    context ={}
    profissional = get_object_or_404(Profissional, id=id_profissional)
    if request.method == 'POST':
        form = ProfissionalForm(request.POST, instance=profissional)
        if form.is_valid():
            form.save()
            return redirect('profissional:list_profissional')
    form = ProfissionalForm(instance=profissional)
    context['form'] = form
    return render(request, template_name, context)

def delete_profissional(request, id_profissional):
    profissional = Profissional.objects.get(id=id_profissional)
    profissional.delete()
    return redirect('profissional:list_profissional')