from django.db import models

from escolas.models.base_model import YearField
from escolas.models.disciplina_model import Disciplina
from escolas.models.sala_model import Sala


class Turma(models.Model):
    nome = models.CharField(max_length=100)
    ano = YearField()
    turno = models.CharField(max_length=10)
    sala = models.ForeignKey(Sala, on_delete=models.CASCADE, related_name='sala_turmas')
    disciplina = models.ManyToManyField(Disciplina, blank=True, related_name='disciplinas_turmas')

    def __str__(self):
        return str(self.nome)

    class Meta:
        unique_together = ['nome', 'ano', 'turno']