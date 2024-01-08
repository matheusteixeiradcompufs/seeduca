from django.db import models

from escolas.models import Disciplina, Turma
from pessoas.models.aluno_model import Aluno
from pessoas.models.boletim_model import Boletim


class Avaliacao(models.Model):
    TIPO_AVALIACAO_CHOICES = [
        ('A1', '1ª Avaliação'),
        ('A2', '2ª Avaliação'),
        ('R1', '1ª Recuperação'),
        ('A3', '3ª Avaliação'),
        ('A4', '4ª Avaliação'),
        ('R2', '2ª Recuperação'),
    ]
    nome = models.CharField(
        max_length=100,
        choices=TIPO_AVALIACAO_CHOICES,
    )
    nota = models.FloatField(
        default=0,
    )
    computada = models.BooleanField(
        default=False,
    )
    aluno = models.ForeignKey(
        Aluno,
        on_delete=models.CASCADE,
        related_name='aluno_avaliacoes',
    )
    disciplina = models.ForeignKey(
        Disciplina,
        on_delete=models.CASCADE,
        related_name='disciplina_avaliacoes',
    )
    boletim = models.ForeignKey(
        Boletim,
        on_delete=models.CASCADE,
        related_name='boletim_avaliacoes',
    )
    turma = models.ForeignKey(
        Turma,
        on_delete=models.CASCADE,
        related_name='turma_avaliacoes',
    )

    def __str__(self):
        return str(self.nome)

    class Meta:
        verbose_name = 'avaliação'
        verbose_name_plural = 'avaliações'