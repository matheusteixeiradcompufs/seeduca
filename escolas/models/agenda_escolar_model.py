from django.db import models

from escolas.models.turma_model import Turma


class AgendaEscolar(models.Model):
    turma = models.OneToOneField(Turma, on_delete=models.CASCADE, related_name='turma_agenda')

    def __str__(self):
        return 'Agenda do ' + str(self.turma)

    class Meta:
        verbose_name = 'agenda escolar'
        verbose_name_plural = 'agendas escolares'