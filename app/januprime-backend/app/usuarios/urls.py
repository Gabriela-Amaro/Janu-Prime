from django.urls import path
from .views import ClienteCadastroView, AdministradorCadastroView

urlpatterns = [
    path("clientes/cadastro/", ClienteCadastroView.as_view(), name="cliente-cadastro"),
    path(
        "administradores/cadastro/",
        AdministradorCadastroView.as_view(),
        name="administrador-cadastro",
    ),
]
