from rest_framework import serializers

from escolas.models import Escola
from escolas.serializers.mural_avisos_serializer import MuralAvisosSerializer
from escolas.serializers.cardapio_serializer import CardapioMerendaSerializer
from escolas.serializers.email_escola_serializer import EmailEscolaSerializer
from escolas.serializers.sala_serializer import SalaSerializer
from escolas.serializers.telefone_escola_serializer import TelefoneEscolaSerializer


class EscolaSerializer(serializers.ModelSerializer):
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
            'objetos_salas',
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
    objetos_salas = SalaSerializer(
        many=True,
        source='escola_salas',
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