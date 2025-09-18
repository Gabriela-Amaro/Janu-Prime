from django.db import models

from django.db import models


class Estabelecimento(models.Model):
    nome = models.CharField(max_length=255)
    endereco = models.CharField(max_length=255, blank=True, unique=True)
    telefone = models.CharField(max_length=15, blank=True, unique=True)
    descricao = models.TextField(blank=True)
    logotipo = models.ImageField(
        upload_to="logotipos/", blank=True
    )  # configurar o upload de imagens depois
    cnpj = models.CharField(
        max_length=18, unique=True, help_text="Formato: 12.345.678/0001-99"
    )
    horario_funcionamento = models.JSONField(
        default=dict, blank=True
    )  # Exemplo: {"segunda": "08:00-18:00", "terça": "08:00-18:00", ...}
    ativo = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome
