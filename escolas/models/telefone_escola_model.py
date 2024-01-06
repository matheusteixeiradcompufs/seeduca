from django.db import models

from escolas.models.base_model import Telefone
from escolas.models.escola_model import Escola


class TelefoneEscola(Telefone):
    escola = models.ForeignKey(Escola, on_delete=models.CASCADE, related_name='escola_telefones')

    def __str__(self):
        return str(self.numero)

    class Meta:
        verbose_name = 'telefone'