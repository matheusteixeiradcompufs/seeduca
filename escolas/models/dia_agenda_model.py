from django.db import models

from escolas.models.agenda_escolar_model import AgendaEscolar
from escolas.models.disciplina_model import Disciplina


class DiaAgenda(models.Model):
    data = models.DateField()
    util = models.BooleanField(default=False)
    disciplinas = models.ManyToManyField(Disciplina, blank=True, related_name='disciplinas_dias')
    agenda = models.ForeignKey(AgendaEscolar, on_delete=models.CASCADE, related_name='agenda_dias')

    def __str__(self):
        return str(self.data)

    class Meta:
        verbose_name = 'dia da agenda'
        verbose_name_plural = 'dias da agenda'
        unique_together = ['data', 'agenda']