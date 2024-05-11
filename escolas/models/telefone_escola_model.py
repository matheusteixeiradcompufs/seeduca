from django.db import models

from escolas.models.base_model import Telefone
from escolas.models.escola_model import Escola

class TelefoneEscola(Telefone):
    """
    Representa um número de telefone associado a uma escola específica.

    Herda de Telefone.
    """

    escola = models.ForeignKey(
        Escola,
        on_delete=models.CASCADE,
        related_name='escola_telefones',
    )
    """
    A escola associada ao número de telefone.
    """

    def __str__(self):
        """
        Retorna uma representação legível do número de telefone.

        Returns:
            str: O número de telefone.
        """
        return str(self.numero)

    class Meta:
        """
        Metadados para a classe TelefoneEscola.
        """
        verbose_name = 'telefone'
        """
        Um nome mais descritivo para este modelo na interface de administração.
        """
