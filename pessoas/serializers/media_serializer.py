from rest_framework import serializers
from escolas.serializers import DisciplinaSerializer
from pessoas.models import Media

class MediaSerializer(serializers.ModelSerializer):
    """
    Serializer para a serialização e desserialização de objetos Media.
    """
    class Meta:
        model = Media
        fields = [
            'id',                   # ID da média
            'tipo',                 # Tipo da média
            'valor',                # Valor da média
            'criada_em',            # Data de criação do registro
            'atualizada_em',        # Data de atualização do registro
            'disciplina',           # Disciplina associada à média
            'boletim',              # Boletim associado à média
            'objeto_disciplina',    # Objeto serializado da disciplina associada
        ]

    objeto_disciplina = DisciplinaSerializer(
        many=False,
        source='disciplina',
        read_only=True,
    )
