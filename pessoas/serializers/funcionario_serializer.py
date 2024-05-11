from rest_framework import serializers
from escolas.serializers.turma_sem_objetos_serializer import TurmaSemObjetosSerializer
from pessoas.models import Funcionario
from pessoas.serializers.telefone_pessoa_serializer import TelefonePessoaSerializer
from pessoas.serializers.email_pessoa_serializer import EmailPessoaSerializer
from pessoas.serializers.usuario_serializer import UsuarioSerializer


class FuncionarioSerializer(serializers.ModelSerializer):
    """
    Serializer para a serialização e desserialização de objetos Funcionario.
    """
    class Meta:
        model = Funcionario
        fields = [
            'id',                   # ID do funcionário
            'matricula',            # Matrícula do funcionário
            'cpf',                  # CPF do funcionário
            'data_nascimento',      # Data de nascimento do funcionário
            'endereco',             # Endereço do funcionário
            'usuario',              # Usuário associado ao funcionário
            'criado_em',            # Data de criação do registro
            'atualizado_em',        # Data de atualização do registro
            'formacao',             # Formação acadêmica do funcionário
            'retrato',              # Retrato do funcionário
            'turmas',               # Turmas associadas ao funcionário
            'uid',                  # UID do funcionário
            'token',                # Token do funcionário
            'objeto_usuario',       # Objeto serializado do usuário associado
            'objetos_telefones',    # Lista de telefones do funcionário
            'objetos_emails',       # Lista de emails do funcionário
            'objetos_turmas',       # Lista de turmas associadas ao funcionário
        ]

    objeto_usuario = UsuarioSerializer(
        many=False,
        source='usuario',
        read_only=True,
    )
    objetos_telefones = TelefonePessoaSerializer(
        many=True,
        source='pessoa_telefones',
        read_only=True,
    )
    objetos_emails = EmailPessoaSerializer(
        many=True,
        source='pessoa_emails',
        read_only=True,
    )
    objetos_turmas = TurmaSemObjetosSerializer(
        many=True,
        source='turmas',
        read_only=True,
    )
