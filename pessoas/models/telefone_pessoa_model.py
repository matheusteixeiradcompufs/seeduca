from django.db import models

from escolas.models import Telefone
from pessoas.models.pessoa_model import Pessoa


class TelefonePessoa(Telefone):
    pessoa = models.ForeignKey(
        Pessoa,
        on_delete=models.CASCADE,
        related_name='pessoa_telefones'
    )

    def __str__(self):
        return str(self.numero)

    class Meta:
        verbose_name = 'telefone'