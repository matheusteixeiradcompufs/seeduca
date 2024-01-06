from django.db import models

from escolas.models import Email
from pessoas.models.pessoa_model import Pessoa


class EmailPessoa(Email):
    pessoa = models.ForeignKey(
        Pessoa,
        on_delete=models.CASCADE,
        related_name='pessoa_emails'
    )

    def __str__(self):
        return str(self.endereco)

    class Meta:
        verbose_name = 'e-mail'