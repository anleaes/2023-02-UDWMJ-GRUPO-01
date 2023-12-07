from django.db import models

# Create your models here.
class Materiais(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    name = models.CharField('Nome', max_length=50)
    description = models.TextField('Descricao', max_length=100)
    doc = models.FileField('Documentos', upload_to='docs')
    
    class Meta:
        verbose_name = 'Materiais'
        verbose_name_plural = 'Materiais'

    def __str__(self):
        return self.name
