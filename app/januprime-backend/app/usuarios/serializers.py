# core/serializers.py

from rest_framework import serializers
from django.db import transaction  

from .models import Usuario, Cliente, Administrador 

# ===================================================================
# SERIALIZERS PARA EXIBIÇÃO DE DADOS (GET requests)
# ===================================================================

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['email', 'tipo_usuario']


class ClienteSerializer(serializers.ModelSerializer):
    usuario = UsuarioSerializer(read_only=True)

    class Meta:
        model = Cliente
        fields = ['usuario', 'nome', 'cpf', 'telefone', 'pontos', 'created_at']


class AdministradorSerializer(serializers.ModelSerializer):
    usuario = UsuarioSerializer(read_only=True)
    # Mostra o nome do estabelecimento em vez de apenas o seu ID
    # estabelecimento = serializers.StringRelatedField() 

    class Meta:
        model = Administrador
        fields = ['usuario', 'nome', 'cpf', 'super_user'] # 'estabelecimento' removido temporariamente


# ===================================================================
# SERIALIZERS PARA CADASTRO (POST requests)
# ===================================================================

class ClienteRegistrationSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(label='Email')
    password = serializers.CharField(write_only=True, required=True, label='Senha', style={'input_type': 'password'})
    password2 = serializers.CharField(write_only=True, required=True, label='Confirme a senha', style={'input_type': 'password'})

    class Meta:
        model = Cliente
        fields = ['email', 'password', 'password2', 'nome', 'cpf', 'telefone']

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "As senhas não coincidem."})
        return attrs

    def create(self, validated_data):
        email = validated_data.pop('email')
        password = validated_data.pop('password')
        validated_data.pop('password2') 

        try:
            with transaction.atomic():
                # Cria o usuário
                usuario = Usuario.objects.create_user(
                    email=email,
                    password=password,
                    tipo_usuario=Usuario.TipoUsuario.CLIENTE
                )
                # Cria o perfil do Cliente
                cliente = Cliente.objects.create(
                    usuario=usuario,
                    **validated_data
                )
        except Exception as e:
            raise serializers.ValidationError(f"Ocorreu um erro durante o registro: {e}")
            
        return cliente


class AdministradorRegistrationSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})
    password2 = serializers.CharField(write_only=True, required=True, label='Confirme a senha', style={'input_type': 'password'})
    # estabelecimento = serializers.PrimaryKeyRelatedField(queryset=Estabelecimento.objects.all())


    class Meta:
        model = Administrador
        fields = ['email', 'password', 'password2', 'nome', 'cpf', 'super_user'] # 'estabelecimento' removido temporariamente
        # fields = ['email', 'password', 'password2', 'nome', 'cpf', 'estabelecimento', 'super_user'] --- IGNORE ---
        
    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "As senhas não coincidem."})
        
        requesting_user = self.context['request'].user
        
        is_creating_superuser = attrs.get('super_user', False)

        if is_creating_superuser and not requesting_user.is_superuser:
            raise serializers.ValidationError(
                "Você não tem permissão para criar um funcionário super-usuário."
            )

        return attrs

    def create(self, validated_data):
        email = validated_data.pop('email')
        password = validated_data.pop('password')
        validated_data.pop('password2')

        try:
            with transaction.atomic():
                # Cria o usuário
                usuario = Usuario.objects.create_user(
                    email=email,
                    password=password,
                    tipo_usuario=Usuario.TipoUsuario.ADMINISTRADOR
                )
                # Cria o perfil do Administrador
                administrador = Administrador.objects.create(
                    usuario=usuario,
                    **validated_data
                )
        except Exception as e:
            raise serializers.ValidationError(f"Ocorreu um erro durante o registro: {e}")

        return administrador