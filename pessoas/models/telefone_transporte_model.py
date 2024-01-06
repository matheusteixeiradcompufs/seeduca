from django.db import models

from escolas.models import Telefone
from pessoas.models.transporte_model import Transporte


class TelefoneTransporte(Telefone):
    transporte = models.ForeignKey(
        Transporte,
        on_delete=models.CASCADE,
        related_name='transporte_telefones',
    )

    def __str__(self):
        return str(self.numero)

    class Meta:
        verbose_name = 'telefone'