from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from .forms import TiposdeprofissionalForm
from .models import Tiposdeprofissional

# Create your views here.

def add_tipodeprofissional(request):
    template_name = 'tiposdeprofissional/add_tipo_de_profissional.html'
    context = {}
    if request.method == 'POST':
        form = TiposdeprofissionalForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            form.save_m2m()
            return redirect('tiposdeprofissional:list_tiposdeprofissional')
    form = TiposdeprofissionalForm()
    context['form'] = form
    return render(request, template_name, context)

def list_tiposdeprofissional(request):
    template_name = 'tiposdeprofissional/list_tipos_de_profissionais.html'
    categories = Tiposdeprofissional.objects.filter()
    context = {
        'tiposdeprofissional': categories
    }
    return render(request, template_name, context)

def edit_tipodeprofissional(request, id_category):
    template_name = 'tiposdeprofissional/add_tipo_de_profissional.html'
    context ={}
    category = get_object_or_404(Tiposdeprofissional, id=id_category)
    if request.method == 'POST':
        form = TiposdeprofissionalForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('tiposdeprofissional:list_tiposdeprofissional')
    form = TiposdeprofissionalForm(instance=category)
    context['form'] = form
    return render(request, template_name, context)

def delete_tipodeprofissional(request, id_category):
    category = Tiposdeprofissional.objects.get(id=id_category)
    category.delete()
    return redirect('tiposdeprofissional:list_tiposdeprofissional')