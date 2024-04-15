from django.db import models

from pessoas.models import Boletim


class Frequencia(models.Model):
    percentual = models.FloatField(
        default=0,
    )
    boletim = models.OneToOneField(
        Boletim,
        on_delete=models.CASCADE,
        related_name='boletim_frequencia',
    )

    def __str__(self):
        return f'Frequência de {self.boletim.aluno} em {self.boletim.turma.ano} da turma {self.boletim.turma}'

    class Meta:
        verbose_name = 'frequência'