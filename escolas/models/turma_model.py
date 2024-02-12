from django.db import models

from escolas.models.base_model import YearField
from escolas.models.disciplina_model import Disciplina
from escolas.models.sala_model import Sala


class Turma(models.Model):
    TURNO_CHOICES = [
        ('M', 'Manhã'),
        ('T', 'Tarde'),
        ('N', 'Noite'),
    ]

    nome = models.CharField(
        max_length=100,
    )
    ano = YearField()
    turno = models.CharField(
        max_length=10,
        choices=TURNO_CHOICES,
    )
    criada_em = models.DateTimeField(
        auto_now_add=True,
    )
    atualizada_em = models.DateTimeField(
        auto_now=True,
    )
    sala = models.ForeignKey(
        Sala,
        on_delete=models.PROTECT,
        related_name='sala_turmas',
    )
    disciplinas = models.ManyToManyField(
        Disciplina,
        blank=True,
        related_name='disciplinas_turmas',
    )

    def __str__(self):
        return f'{str(self.nome)} em {self.ano}'

    class Meta:
        unique_together = ['nome', 'ano', 'turno']