from django.db import models

from escolas.models import Telefone
from pessoas.models.pessoa_model import Pessoa


class TelefonePessoa(Telefone):
    """
    Modelo que representa um telefone associado a uma pessoa.

    Atributos:
        pessoa (ForeignKey): A pessoa associada ao telefone.
    """

    pessoa = models.ForeignKey(
        Pessoa,
        on_delete=models.CASCADE,
        related_name='pessoa_telefones',
        verbose_name='pessoa'
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
