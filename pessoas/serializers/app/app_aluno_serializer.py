from rest_framework import serializers

from pessoas.models import Aluno
from pessoas.serializers.app.app_boletim_serializer import AppBoletimSerializer
from pessoas.serializers.telefone_pessoa_serializer import TelefonePessoaSerializer
from pessoas.serializers.email_pessoa_serializer import EmailPessoaSerializer
from pessoas.serializers.responsavel_serializer import ResponsavelSerializer
from pessoas.serializers.transporte_serializer import TransporteSerializer
from pessoas.serializers.usuario_serializer import UsuarioSerializer


class AppAlunoSerializer(serializers.ModelSerializer):
    """
        Serializer para a model Aluno. Exclusivo para a API Restful do app mobile.

        Este serializer é usado para serializar e desserializar instâncias
        da model Aluno. Ele inclui campos relacionados a dados pessoais
        do aluno, bem como informações sobre o usuário associado, telefones,
        e-mails, responsáveis, boletins e transportes do aluno.

        Fields:
            id (int): ID do aluno.
            matricula (str): Número de matrícula do aluno.
            cpf (str): CPF do aluno.
            data_nascimento (date): Data de nascimento do aluno.
            usuario (dict): Dados do usuário associado ao aluno.
            endereco (str): Endereço do aluno.
            criado_em (datetime): Data e hora de criação do registro.
            atualizado_em (datetime): Data e hora da última atualização do registro.
            eh_pcd (bool): Indica se o aluno é uma pessoa com deficiência.
            descricao_pcd (str): Descrição da deficiência, se aplicável.
            retrato (str): URL da imagem do aluno.
            objeto_usuario (dict): Dados do usuário associado ao aluno.
            objetos_telefones (list): Lista de telefones associados ao aluno.
            objetos_emails (list): Lista de e-mails associados ao aluno.
            objetos_responsaveis (list): Lista de responsáveis pelo aluno.
            objetos_boletins (list): Lista de boletins do aluno.
            objetos_transportes (list): Lista de transportes utilizados pelo aluno.
        """

    class Meta:
        model = Aluno
        fields = [
            'id',
            'matricula',
            'cpf',
            'data_nascimento',
            'usuario',
            'endereco',
            'criado_em',
            'atualizado_em',
            'eh_pcd',
            'descricao_pcd',
            'retrato',
            'objeto_usuario',
            'objetos_telefones',
            'objetos_emails',
            'objetos_responsaveis',
            'objetos_boletins',
            'objetos_transportes',
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
    objetos_responsaveis = ResponsavelSerializer(
        many=True,
        source='aluno_responsaveis',
        read_only=True,
    )
    objetos_boletins = AppBoletimSerializer(
        many=True,
        source='aluno_boletins',
        read_only=True,
    )
    objetos_transportes = TransporteSerializer(
        many=True,
        source='alunos_transportes',
        read_only=True,
    )