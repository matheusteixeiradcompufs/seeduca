from django.db import models

from escolas.models import YearField
from pessoas.models.aluno_model import Aluno


class AgendaRecados(models.Model):
    ano = YearField()
    aluno = models.ForeignKey(
        Aluno,
        on_delete=models.CASCADE,
        related_name='aluno_agendas'
    )

    def __str__(self):
        return f'Agenda de Recados de {self.ano}'

    class Meta:
        verbose_name = 'agenda de recados'
        verbose_name_plural = 'agendas de recados'
