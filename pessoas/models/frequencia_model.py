from django.db import models

from escolas.models import YearField
from pessoas.models.aluno_model import Aluno


class Frequencia(models.Model):
    ano = YearField()
    percentual = models.FloatField(
        blank=True,
        null=True
    )
    aluno = models.ForeignKey(
        Aluno,
        on_delete=models.CASCADE,
        related_name='aluno_frequencias'
    )

    def __str__(self):
        return 'Frequência de ' + self.aluno.usuario.first_name + 'em ' + str(self.ano)

    class Meta:
        verbose_name = 'frequência'
        unique_together = ['ano', 'aluno']