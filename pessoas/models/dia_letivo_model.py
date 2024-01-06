from django.db import models

from pessoas.models.frequencia_model import Frequencia


class DiaLetivo(models.Model):
    data = models.DateField()
    presenca = models.BooleanField(default=True)
    frequencia = models.ForeignKey(
        Frequencia,
        on_delete=models.CASCADE,
        related_name='frequencia_diasletivos',
    )

    def __str__(self):
        return str(self.data)

    class Meta:
        verbose_name = 'dia letivo'
        verbose_name_plural = 'dias letivos'
        unique_together = ['data', 'frequencia']