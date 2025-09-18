from django.urls import path
from .views import ClienteCadastroView, AdministradorRegisterView

urlpatterns = [
    path("clientes/cadastro/", ClienteCadastroView.as_view(), name="cliente-cadastro"),
    path(
        "administradores/cadastro/",
        AdministradorRegisterView.as_view(),
        name="administrador-cadastro",
    ),
]
