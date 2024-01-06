from django.db import models

from escolas.models import YearField
from pessoas.models.aluno_model import Aluno


class Boletim(models.Model):
    ano = YearField()
    aluno = models.ForeignKey(
        Aluno,
        on_delete=models.CASCADE,
        related_name='aluno_boletins'
    )

    def __str__(self):
        return 'Boletim de ' + str(self.aluno.usuario.first_name) + ' em ' + str(self.ano)

    class Meta:
        verbose_name_plural = 'boletins'
        unique_together = ['ano', 'aluno']