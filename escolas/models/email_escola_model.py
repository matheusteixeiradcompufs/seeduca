from django.db import models

from escolas.models.base_model import Email
from escolas.models.escola_model import Escola


class EmailEscola(Email):
    escola = models.ForeignKey(Escola, on_delete=models.CASCADE, related_name='escola_emails')

    def __str__(self):
        return str(self.endereco)

    class Meta:
        verbose_name = 'e-mail'