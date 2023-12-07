from django.db import models
from materiais.models import Materiais
from clients.models import Client
#import profissional
#import servico

# Create your models here.

class Atendimentos(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    total_price = models.FloatField('Preco Total', null=True, blank=True, default=0.0)
    STATUS_CHOICES = (
        ('Em andamento', 'Em andamento'),
        ('Finalizado', 'Finalizado'),
        ('Cancelado', 'Cancelado'),
    )
    status = models.CharField('Status', max_length=20, choices=STATUS_CHOICES, null=True, blank=True, default='Em andamento')
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    #materiais_atendimento = models.ForeignKey(MateriaisAtendimentoForm, through='materiais atendimentos', blank=True)
    #profissional
    #servico

    class Meta:
        verbose_name = 'Atendimento'
        verbose_name_plural = 'Atendimentos'
        ordering =['-created_on']

    def __str__(self):
        return "%s" % (self.total_price) 


class MateriaisAtendimentos(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    quantity = models.IntegerField('Quantidade',null=True, blank=True,default=0)
    unitary_price = models.FloatField('Preco unitario',null=True, blank=True, default=0.0)
    atendimento = models.ForeignKey(Atendimentos, on_delete=models.CASCADE)
    material = models.ForeignKey(Materiais, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Material do atendimento'
        verbose_name_plural = 'Materiais do atendimento'
        ordering =['id']

    def __str__(self):
        return "%s" % (self.quantity) 