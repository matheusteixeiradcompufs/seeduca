from django.contrib.auth.models import User, Group
from rest_framework import serializers

from escolas.serializers import TelefoneSerializer, EmailSerializer, EscolaSerializer
from pessoas.models import Aluno, Funcionario, Responsavel, Boletim, Avaliacao, Frequencia, DiaLetivo, Transporte, \
    TelefonePessoa, EmailPessoa, TelefoneTransporte


class TelefonePessoaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TelefonePessoa
        fields = [
            'id',
            'numero',
            'pessoa',
        ]


class EmailPessoaSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmailPessoa
        fields = [
            'id',
            'endereco',
            'pessoa',
        ]


class GrupoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = [
            'id',
            'name',
        ]


class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'first_name',
            'last_name',
            'email',
            'password',
            'grupos',
        ]
        extra_kwargs = {
            'password': {
                'write_only': True
            }
        }

    grupos = GrupoSerializer(
        many=True,
        source='groups',
        read_only=True,
    )

    def create(self, validated_data):

        grupos = self.initial_data.pop('grupos_add', [])

        user = User.objects.create_user(**validated_data)

        for grupo_nome in grupos:
            grupo = Group.objects.get(name=grupo_nome)
            user.groups.add(grupo)

        return user

    def update(self, instance, validated_data):

        grupos_add = self.initial_data.pop('grupos_add', [])

        for grupo_nome in grupos_add:
            grupo = Group.objects.get(name=grupo_nome)
            instance.groups.add(grupo)

        grupos_remove = self.initial_data.pop('grupos_remove', [])

        for grupo_nome in grupos_remove:
            grupo = Group.objects.get(name=grupo_nome)
            instance.groups.remove(grupo)

        return super(UsuarioSerializer, self).update(instance, validated_data)


class ResponsavelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Responsavel
        fields = [
            'id',
            'cpf',
            'nome',
            'observacao',
            'aluno',
        ]


class AvaliacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Avaliacao
        fields = [
            'id',
            'nome',
            'nota',
            'aluno',
            'disciplina',
            'boletim',
            'turma',
        ]


class BoletimSerializer(serializers.ModelSerializer):
    class Meta:
        model = Boletim
        fields = [
            'id',
            'ano',
            'aluno',
            'objetos_avaliacoes',
        ]

    objetos_avaliacoes = AvaliacaoSerializer(
        many=True,
        source='boletim_avaliacoes',
        read_only=True,
    )


class DiaLetivoSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiaLetivo
        fields = [
            'id',
            'data',
            'presenca',
            'frequencia',
        ]


class FrequenciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Frequencia
        fields = [
            'id',
            'ano',
            'percentual',
            'aluno',
            'objetos_diasletivos',
        ]
    objetos_diasletivos = DiaLetivoSerializer(
        many=True,
        source='frequencia_diasletivos',
        read_only=True,
    )


class TelefoneTransporteSerializer(serializers.ModelSerializer):
    class Meta:
        model = TelefoneTransporte
        fields = [
            'id',
            'numero',
            'transporte',
        ]


class TransporteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transporte
        fields = [
            'id',
            'placa',
            'ano',
            'tipo',
            'nomeMotorista',
            'nomeAuxiliar',
            'itinerario',
            'aluno',
            'objetos_telefones',
        ]
    objetos_telefones = TelefoneSerializer(
        many=True,
        source='transporte_telefones',
        read_only=True,
    )


def criar_usuario(classe, classe_data, usuario_data):
    usuario_serializer = UsuarioSerializer(data=usuario_data)
    if usuario_serializer.is_valid():
        usuario = usuario_serializer.save()

        usuario_classe = classe.objects.create(usuario=usuario, **classe_data)
        return usuario_classe


def atualizar_usuario(instance, validated_data, usuario_data):
    usuario_serializer = UsuarioSerializer(instance=instance.usuario, data=usuario_data, partial=True)
    if usuario_serializer.is_valid():
        usuario_serializer.save()

    # Agora, atualize os campos em `Funcionario`
    for key, value in validated_data.items():
        setattr(instance, key, value)

    instance.save()

    return instance


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
            'turma',
            'objeto_escola',
            'objeto_usuario',
            'objetos_telefones',
            'objetos_emails',
            'objetos_responsaveis',
            'objetos_boletins',
            'objetos_frequencias',
            'objetos_transportes',
            # 'objetos_turmas',
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
    objetos_telefones = TelefoneSerializer(
        many=True,
        source='pessoa_telefones',
        read_only=True,
    )
    objetos_emails = EmailSerializer(
        many=True,
        source='pessoa_emails',
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
    # objetos_turmas = TurmaSerializer(
    #     many=True,
    #     source='turma',
    #     read_only=True,
    # )

    def create(self, validated_data):

        usuario_data = validated_data.pop('usuario', {})

        return criar_usuario(Aluno, validated_data, usuario_data)

    def update(self, instance, validated_data):

        usuario_data = validated_data.pop('usuario', {})

        instance = atualizar_usuario(instance, validated_data, usuario_data)

        return super(AlunoSerializer, self).update(instance, validated_data)


class FuncionarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Funcionario
        fields = [
            'id',
            'matricula',
            'cpf',
            'data_nascimento',
            'endereco',
            'formacao',
            'escola',
            'turma',
            'objeto_escola',
            'objeto_usuario',
            'objetos_telefones',
            'objetos_emails',
            # 'objetos_turmas',
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
    objetos_telefones = TelefoneSerializer(
        many=True,
        source='pessoa_telefones',
        read_only=True,
    )
    objetos_emails = EmailSerializer(
        many=True,
        source='pessoa_emails',
        read_only=True,
    )
    # objetos_turmas = TurmaSerializer(
    #     many=True,
    #     source='turma',
    #     read_only=True,
    # )

    def create(self, validated_data):

        # Atualize os campos diretamente em `usuario`
        grupos_add = self.initial_data.pop('grupos_add', [])

        usuario_data = validated_data.pop('usuario', {})

        usuario_data['grupos_add'] = grupos_add

        return criar_usuario(Funcionario, validated_data, usuario_data)

    def update(self, instance, validated_data):

        # Atualize os campos diretamente em `usuario`
        grupos_add = self.initial_data.pop('grupos_add', [])
        grupos_remove = self.initial_data.pop('grupos_remove', [])

        usuario_data = validated_data.pop('usuario', {})

        usuario_data['grupos_add'] = grupos_add
        usuario_data['grupos_remove'] = grupos_remove

        instance = atualizar_usuario(instance, validated_data, usuario_data)

        return super(FuncionarioSerializer, self).update(instance, validated_data)
