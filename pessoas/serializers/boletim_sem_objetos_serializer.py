from rest_framework import serializers

from pessoas.models import Boletim


class BoletimSemObjetosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Boletim
        fields = [
            'id',
            'aluno',
            'status',
            'encerrar',
            'qr_code',
            'turma',
        ]
