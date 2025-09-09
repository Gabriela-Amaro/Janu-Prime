from rest_framework import serializers
from .models import Cliente

class ClienteCadastroSerializer(serializers.ModelSerializer):
    """
    Serializer para o cadastro de um novo Cliente.
    Ele é simples porque o modelo Cliente já contém toda a lógica necessária.
    """

    # A senha é um campo de entrada, mas não queremos que ela seja retornada
    # na resposta, por isso é 'write_only'.
    senha = serializers.CharField(write_only=True, style={'input_type': 'password'}, min_length=8)

    class Meta:
        model = Cliente
        # Lista de campos que o serializer vai usar para entrada e saída.
        # A 'senha' é usada na entrada, mas não na saída.
        fields = ['id', 'nome', 'email', 'cpf', 'telefone', 'pontos', 'senha']
        
        # 'id' e 'pontos' são gerados automaticamente, então são apenas para leitura.
        read_only_fields = ['id', 'pontos']

