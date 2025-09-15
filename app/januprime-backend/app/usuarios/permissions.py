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
    return is_admin and hasattr(request.user, 'administrador') and request.user.administrador.super_user

class CanRegisterAdministrador(BasePermission):
    message = "Você não tem permissão para cadastrar novos funcionários."

    def has_permission(self, request, view):
        if not (request.user and request.user.is_authenticated):
            return False

        if request.user.is_superuser:
            return True

        if request.user.tipo_usuario == Usuario.TipoUsuario.ADMINISTRADOR:
            # hasattr previne erro caso o perfil ainda não exista por algum motivo
            if hasattr(request.user, 'administrador') and request.user.administrador.super_user:
                return True
        
        return False