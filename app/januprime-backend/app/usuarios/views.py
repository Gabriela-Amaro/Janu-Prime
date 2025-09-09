from rest_framework import generics, permissions
from .models import Cliente
from .serializers import ClienteCadastroSerializer

class ClienteCadastroView(generics.CreateAPIView):
    """
    View para o endpoint de cadastro de novos clientes.
    """
    queryset = Cliente.objects.all()
    serializer_class = ClienteCadastroSerializer
    permission_classes = [permissions.AllowAny] # Permite que qualquer um se cadastre.