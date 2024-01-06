from rest_framework import serializers

from pessoas.models import TelefoneTransporte


class TelefoneTransporteSerializer(serializers.ModelSerializer):
    class Meta:
        model = TelefoneTransporte
        fields = [
            'id',
            'numero',
            'transporte',
        ]