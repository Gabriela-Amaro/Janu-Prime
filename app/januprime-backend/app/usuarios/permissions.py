# core/permissions.py
from rest_framework.permissions import BasePermission
from .models import Usuario

class IsCliente(BasePermission):
  def has_permission(self, request, view):
    return (request.user and request.user.is_authenticated and
      request.user.tipo_usuario == Usuario.TipoUsuario.CLIENTE)

class IsAdministrador(BasePermission):
  def has_permission(self, request, view):
    return (request.user and request.user.is_authenticated and
      request.user.tipo_usuario == Usuario.TipoUsuario.ADMINISTRADOR)

class IsSuperUserAdministrador(BasePermission):
  def has_permission(self, request, view):
    is_admin = IsAdministrador().has_permission(request, view)
    # Verifica se é um administrador e se a flag super_user do seu perfil está ativa
    return is_admin and hasattr(request.user, 'administrador') and request.user.administrador.super_user