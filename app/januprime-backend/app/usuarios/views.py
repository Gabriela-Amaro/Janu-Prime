from rest_framework import generics, permissions, status
from rest_framework.response import Response
from .models import Cliente, Administrador
from .serializers import (
    ClienteRegistrationSerializer,
    ClienteSerializer,
    AdministradorRegistrationSerializer,
    AdministradorSerializer,
    ChangePasswordSerializer,
)
from .permissions import (
    CanRegisterAdministrador, 
    IsClienteOwner, 
    IsAdministradorOwnerOrSameEstablishmentSuperUser
)

class ClienteCadastroView(generics.CreateAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteRegistrationSerializer
    permission_classes = [permissions.AllowAny]

    def create(self, request, *args, **kwargs):
        reg_serializer = self.get_serializer(data=request.data)
        reg_serializer.is_valid(raise_exception=True)
        cliente_instance = reg_serializer.save()

        display_serializer = ClienteSerializer(
            cliente_instance, context=self.get_serializer_context()
        )

        headers = self.get_success_headers(display_serializer.data)

        return Response(
            display_serializer.data, status=status.HTTP_201_CREATED, headers=headers
        )


class AdministradorCadastroView(generics.CreateAPIView):
    queryset = Administrador.objects.all()
    serializer_class = AdministradorRegistrationSerializer
    permission_classes = [CanRegisterAdministrador]

    def create(self, request, *args, **kwargs):
        reg_serializer = self.get_serializer(data=request.data)
        reg_serializer.is_valid(raise_exception=True)
        admin_instance = reg_serializer.save()

        display_serializer = AdministradorSerializer(
            admin_instance, context=self.get_serializer_context()
        )

        headers = self.get_success_headers(display_serializer.data)

        return Response(
            display_serializer.data, status=status.HTTP_201_CREATED, headers=headers
        )



class ClienteDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    permission_classes = [permissions.IsAuthenticated, IsClienteOwner]

    def perform_destroy(self, instance):
        instance.usuario.delete()


class AdministradorDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Administrador.objects.all()
    serializer_class = AdministradorSerializer
    permission_classes = [permissions.IsAuthenticated, IsAdministradorOwnerOrSameEstablishmentSuperUser]

    def perform_destroy(self, instance):
        instance.usuario.delete()
    

class ChangePasswordView(generics.UpdateAPIView):
    serializer_class = ChangePasswordSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self, queryset=None):
        return self.request.user

    def update(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({"detail": "Senha alterada com sucesso."}, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)