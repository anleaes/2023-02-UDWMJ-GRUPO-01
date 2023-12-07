from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from .forms import MateriaisForm
from .models import Materiais
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/contas/login/')
def add_materiais(request):
    template_name = 'materiais/add_materiais.html'
    context = {}
    if request.method == 'POST':
        form = MateriaisForm(request.POST, request.FILES)
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            form.save_m2m()
            return redirect('materiais:list_materiais')
    form = MateriaisForm()
    context['form'] = form
    return render(request, template_name, context)

def list_materiais(request):
    template_name = 'materiais/list_materiais.html'
    materiais = Materiais.objects.filter()
    context = {
        'materiais': materiais
    }
    return render(request, template_name, context)

@login_required(login_url='/contas/login/')
def edit_materiais(request, id_materiais):
    template_name = 'materiais/add_materiais.html'
    context ={}
    materiais = get_object_or_404(Materiais, id=id_materiais)
    if request.method == 'POST':
        form = MateriaisForm(request.POST, request.FILES,  instance=materiais)
        if form.is_valid():
            form.save()
            return redirect('materiais:list_materiais')
    form = MateriaisForm(instance=materiais)
    context['form'] = form
    return render(request, template_name, context)

@login_required(login_url='/contas/login/')
def delete_materiais(request, id_materiais):
    materiais = Materiais.objects.get(id=id_materiais)
    materiais.delete()
    return redirect('materiais:list_materiais')
