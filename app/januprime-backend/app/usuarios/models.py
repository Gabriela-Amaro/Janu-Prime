# core/models.py
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models

# --- GERENCIADOR DO USUÁRIO CENTRAL ---
class UsuarioManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('O usuário deve ter um endereço de e-mail')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

# --- MODELO DE USUÁRIO CENTRAL PARA AUTENTICAÇÃO. Contém apenas os dados de login.---
class Usuario(AbstractBaseUser, PermissionsMixin):
    class TipoUsuario(models.TextChoices):
        CLIENTE = 'CLIENTE', 'Cliente'
        ADMINISTRADOR = 'ADMINISTRADOR', 'Administrador' # Engloba Funcionário e Superuser
        ADM_PLATAFORMA = 'ADM_PLATAFORMA', 'Admin da Plataforma'

    email = models.EmailField(unique=True)
    tipo_usuario = models.CharField(max_length=20, choices=TipoUsuario.choices)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False) # Necessário para o admin do Django

    objects = UsuarioManager()

    USERNAME_FIELD = 'email' # Usa o e-mail para login

    def __str__(self):
        return self.email

class Cliente(models.Model):
    # Relação 1-para-1 com o usuário de autenticação
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE, primary_key=True)
    nome = models.CharField(max_length=255)
    cpf = models.CharField(max_length=14)
    telefone = models.CharField(max_length=20)
    pontos = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome

class Administrador(models.Model):
    # Relação 1-para-1 com o usuário de autenticação
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE, primary_key=True)
    # estabelecimento = models.ForeignKey(Estabelecimento, on_delete=models.PROTECT)
    nome = models.CharField(max_length=255)
    cpf = models.CharField(max_length=14)
    ativo = models.BooleanField(default=True)
    super_user = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome