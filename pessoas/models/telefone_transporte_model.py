from django.db import models

from escolas.models import Telefone
from pessoas.models.transporte_model import Transporte


class TelefoneTransporte(Telefone):
    """
    Modelo que representa um telefone associado a um meio de transporte.

    Atributos:
        transporte (ForeignKey): O meio de transporte associado ao telefone.
    """

    transporte = models.ForeignKey(
        Transporte,
        on_delete=models.CASCADE,
        related_name='transporte_telefones',
        verbose_name='transporte'
    )

    def __str__(self):
        """
        Retorna uma representação legível do telefone.

        Returns:
            str: Uma string representando o número do telefone.
        """
        return str(self.numero)

    class Meta:
        # Nome legível para o modelo
        verbose_name = 'telefone'
