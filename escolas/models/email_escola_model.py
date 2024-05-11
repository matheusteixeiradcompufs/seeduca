from django.db import models

from escolas.models.base_model import Email
from escolas.models.escola_model import Escola


class EmailEscola(Email):
    """
    Representa um endereço de email associado a uma escola específica.

    Herda de Email.
    """

    escola = models.ForeignKey(
        Escola,
        on_delete=models.CASCADE,
        related_name='escola_emails',
    )
    """
    A escola associada a este endereço de email.
    """

    def __str__(self):
        """
        Retorna uma representação legível do endereço de email.

        Returns:
            str: O endereço de email.
        """
        return str(self.endereco)

    class Meta:
        """
        Metadados para a classe EmailEscola.
        """
        verbose_name = 'e-mail'
        """
        Um nome mais descritivo para este modelo na interface de administração.
        """
