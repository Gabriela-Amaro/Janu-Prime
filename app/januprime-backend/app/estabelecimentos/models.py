from django.db import models

# Create your models here.
from django.db import models

class Estabelecimento(models.Model):
    nome = models.CharField(max_length=255)
    cnpj = models.CharField(max_length=18, unique=True, help_text="Formato: 12.345.678/0001-99")
    endereco = models.CharField(max_length=255, blank=True)
    telefone = models.CharField(max_length=15, blank=True)
    descricao = models.TextField(blank=True)
    logotipo = models.ImageField(upload_to='logotipos/') # Precisaremos configurar o upload de imagens depois
    horario_funcionamento = models.CharField(max_length=100, blank=True)
    ativo = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome
