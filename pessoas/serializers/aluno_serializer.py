from rest_framework import serializers

from escolas.serializers import EscolaSerializer, TurmaSerializer
from pessoas.models import Aluno
from pessoas.serializers import AgendaRecadosSerializer
from pessoas.serializers.telefone_pessoa_serializer import TelefonePessoaSerializer
from pessoas.serializers.email_pessoa_serializer import EmailPessoaSerializer
from pessoas.serializers.responsavel_serializer import ResponsavelSerializer
from pessoas.serializers.boletim_serializer import BoletimSerializer
from pessoas.serializers.frequencia_serializer import FrequenciaSerializer
from pessoas.serializers.transporte_serializer import TransporteSerializer
from pessoas.serializers.usuario_serializer import UsuarioSerializer, criar_usuario, atualizar_usuario


class AlunoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aluno
        fields = [
            'id',
            'matricula',
            'cpf',
            'data_nascimento',
            'endereco',
            'eh_pcd',
            'descricao_pcd',
            'escola',
            'turmas',
            'objeto_escola',
            'objeto_usuario',
            'objetos_telefones',
            'objetos_emails',
            'objetos_agendas',
            'objetos_responsaveis',
            'objetos_boletins',
            'objetos_frequencias',
            'objetos_transportes',
            'objetos_turmas',
        ]

    objeto_escola = EscolaSerializer(
        many=False,
        source='escola',
        read_only=True,
    )
    objeto_usuario = UsuarioSerializer(
        many=False,
        source='usuario',
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
    objetos_agendas = AgendaRecadosSerializer(
        many=True,
        source='aluno_agendas',
        read_only=True,
    )
    objetos_responsaveis = ResponsavelSerializer(
        many=True,
        source='aluno_responsaveis',
        read_only=True,
    )
    objetos_boletins = BoletimSerializer(
        many=True,
        source='aluno_boletins',
        read_only=True,
    )
    objetos_frequencias = FrequenciaSerializer(
        many=True,
        source='aluno_frequencias',
        read_only=True,
    )
    objetos_transportes = TransporteSerializer(
        many=True,
        source='alunos_transportes',
        read_only=True,
    )
    objetos_turmas = TurmaSerializer(
        many=True,
        source='turmas',
        read_only=True,
    )

    def create(self, validated_data):

        usuario_data = validated_data.pop('usuario', {})

        return criar_usuario(Aluno, validated_data, usuario_data)

    def update(self, instance, validated_data):

        usuario_data = validated_data.pop('usuario', {})

        instance = atualizar_usuario(instance, validated_data, usuario_data)

        return super(AlunoSerializer, self).update(instance, validated_data)