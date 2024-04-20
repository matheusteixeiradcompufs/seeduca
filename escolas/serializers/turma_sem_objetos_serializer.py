from rest_framework import serializers

from escolas.models import Turma


class TurmaSemObjetosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Turma
        fields = [
            'id',
            'nome',
            'ano',
            'turno',
            'criada_em',
            'atualizada_em',
            'sala',
            'disciplinas',
        ]