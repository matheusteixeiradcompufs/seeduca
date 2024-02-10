from django.db import models

from escolas.models import YearField


class Frequencia(models.Model):
    percentual = models.FloatField(
        default=0,
    )

    def __str__(self):
        return 'Frequência'

    class Meta:
        verbose_name = 'frequência'