from rest_framework import serializers

from pessoas.models import Recado


class RecadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recado
        fields = [
            'id',
            'texto',
            'eh_aluno',
            'publicado_em',
            'pessoa',
            'agenda',
        ]