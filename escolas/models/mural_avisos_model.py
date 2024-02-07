from django.db import models

from escolas.models.base_model import YearField
from escolas.models.escola_model import Escola


class MuralAvisos(models.Model):
    ano = YearField(
        unique=True,
    )
    escola = models.ForeignKey(
        Escola,
        on_delete=models.CASCADE,
        related_name='escola_murais',
    )

    class Meta:
        verbose_name = 'mural de avisos'
        verbose_name_plural = 'Murais de avisos'
