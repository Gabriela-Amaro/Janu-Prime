from rest_framework import generics, permissions, status
from rest_framework.response import Response
from .models import Cliente, Administrador
from .serializers import ClienteRegistrationSerializer, ClienteSerializer, AdministradorRegistrationSerializer, AdministradorSerializer
from .permissions import CanRegisterAdministrador 


class ClienteCadastroView(generics.CreateAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteRegistrationSerializer
    permission_classes = [permissions.AllowAny]

    def create(self, request, *args, **kwargs):
        reg_serializer = self.get_serializer(data=request.data)
        reg_serializer.is_valid(raise_exception=True)
        cliente_instance = reg_serializer.save()

        display_serializer = ClienteSerializer(cliente_instance, context=self.get_serializer_context())
        
        headers = self.get_success_headers(display_serializer.data)
        
        return Response(display_serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class AdministradorRegisterView(generics.CreateAPIView):
    queryset = Administrador.objects.all()
    serializer_class = AdministradorRegistrationSerializer
    permission_classes = [CanRegisterAdministrador]

    def create(self, request, *args, **kwargs):
        reg_serializer = self.get_serializer(data=request.data)
        reg_serializer.is_valid(raise_exception=True)
        admin_instance = reg_serializer.save()

        display_serializer = AdministradorSerializer(admin_instance, context=self.get_serializer_context())
        
        headers = self.get_success_headers(display_serializer.data)
        
        return Response(display_serializer.data, status=status.HTTP_201_CREATED, headers=headers)