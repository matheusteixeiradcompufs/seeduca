from rest_framework import serializers

from pessoas.models import Media


class MediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Media
        fields = [
            'id',
            'tipo',
            'valor',
            'disciplina',
            'boletim',
        ]