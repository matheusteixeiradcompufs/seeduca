from django.db import models

from escolas.models import Disciplina, Turma
from pessoas.models.aluno_model import Aluno
from pessoas.models.boletim_model import Boletim


class Avaliacao(models.Model):
    nome = models.CharField(
        max_length=100
    )
    nota = models.FloatField(
        blank=True,
        null=True,
    )
    aluno = models.ForeignKey(
        Aluno,
        on_delete=models.CASCADE,
        related_name='aluno_avaliacoes'
    )
    disciplina = models.ForeignKey(
        Disciplina,
        on_delete=models.CASCADE,
        related_name='disciplina_avaliacoes'
    )
    boletim = models.ForeignKey(
        Boletim,
        on_delete=models.CASCADE,
        related_name='boletim_avaliacoes'
    )
    turma = models.ForeignKey(
        Turma,
        on_delete=models.CASCADE,
        related_name='turma_avaliacoes'
    )

    def __str__(self):
        return str(self.nome)

    class Meta:
        verbose_name = 'avaliação'
        verbose_name_plural = 'avaliações'