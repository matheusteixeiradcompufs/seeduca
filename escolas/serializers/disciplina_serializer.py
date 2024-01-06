from rest_framework import serializers

from escolas.models import Disciplina


class DisciplinaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Disciplina
        fields = [
            'id',
            'nome',
        ]