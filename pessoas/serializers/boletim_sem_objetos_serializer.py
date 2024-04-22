from rest_framework import serializers

from pessoas.models import Boletim
from pessoas.serializers.aluno_sem_objetos_serializer import AlunoSemObjetosSerializer


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
            'objeto_aluno',
        ]

    objeto_aluno = AlunoSemObjetosSerializer(
        many=False,
        source='aluno',
        read_only=True,
    )
