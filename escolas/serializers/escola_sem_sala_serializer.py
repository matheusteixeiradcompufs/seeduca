from rest_framework import serializers
from escolas.models import Escola
from escolas.serializers.cardapio_serializer import CardapioMerendaSerializer
from escolas.serializers.mural_avisos_serializer import MuralAvisosSerializer
from escolas.serializers.email_escola_serializer import EmailEscolaSerializer
from escolas.serializers.telefone_escola_serializer import TelefoneEscolaSerializer


class EscolaSemSalaSerializer(serializers.ModelSerializer):
    """
    Serializer para a model Escola.

    Este serializer é usado para serializar/desserializar instâncias de Escola.
    Ele inclui os relacionamentos com as models TelefoneEscolaSerializer, EmailEscolaSerializer,
    CardapioMerendaSerializer e MuralAvisosSerializer para serialização de telefones, e-mails,
    cardápios de merenda e murais de avisos associados à escola.

    Atributos:
        id (int): O identificador único da escola.
        cnpj (str): O CNPJ da escola.
        nome (str): O nome da escola.
        endereco (str): O endereço da escola.
        num_salas (int): O número de salas na escola.
        quantidade_alunos (int): A quantidade de alunos na escola.
        descricao (str): A descrição da escola.
        criado_em (datetime): A data e hora de criação da escola.
        atualizado_em (datetime): A data e hora da última atualização da escola.
        imagem (str): O caminho para a imagem da escola.
        objetos_telefones (list): Uma lista de objetos telefones associados à escola.
        objetos_emails (list): Uma lista de objetos e-mails associados à escola.
        objetos_cardapios (list): Uma lista de objetos cardápios de merenda associados à escola.
        objetos_murais (list): Uma lista de objetos murais de avisos associados à escola.
    """
    class Meta:
        model = Escola
        fields = [
            'id',
            'cnpj',
            'nome',
            'endereco',
            'num_salas',
            'quantidade_alunos',
            'descricao',
            'criado_em',
            'atualizado_em',
            'imagem',
            'objetos_telefones',
            'objetos_emails',
            'objetos_cardapios',
            'objetos_murais',
        ]

    objetos_telefones = TelefoneEscolaSerializer(
        many=True,
        source='escola_telefones',
        read_only=True,
    )
    objetos_emails = EmailEscolaSerializer(
        many=True,
        source='escola_emails',
        read_only=True,
    )
    objetos_cardapios = CardapioMerendaSerializer(
        many=True,
        source='escola_cardapios',
        read_only=True,
    )
    objetos_murais = MuralAvisosSerializer(
        many=True,
        source='escola_murais',
        read_only=True,
    )
