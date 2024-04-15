from django.db import models

from pessoas.models.boletim_model import Boletim


class AgendaRecados(models.Model):
    boletim = models.OneToOneField(
        Boletim,
        on_delete=models.CASCADE,
        related_name='boletim_agendas',
    )

    def __str__(self):
        return f'Agenda de Recados de {self.boletim.turma.ano}'

    class Meta:
        verbose_name = 'agenda de recados'
        verbose_name_plural = 'agendas de recados'
