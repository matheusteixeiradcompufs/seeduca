from django.db import models
from escolas.models import Email
from pessoas.models.pessoa_model import Pessoa


class EmailPessoa(Email):
    """
    Model para representar o e-mail de uma pessoa.

    Atributos:
        pessoa (ForeignKey): A referência à pessoa associada ao e-mail.
    """

    pessoa = models.ForeignKey(
        Pessoa,
        on_delete=models.CASCADE,
        related_name='pessoa_emails',
        verbose_name='pessoa'
    )

    def __str__(self):
        """
        Retorna uma representação legível do e-mail da pessoa.

        Returns:
            str: O endereço de e-mail da pessoa.
        """
        return str(self.endereco)

    class Meta:
        verbose_name = 'e-mail'
