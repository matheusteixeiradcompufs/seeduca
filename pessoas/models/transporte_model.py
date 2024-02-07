from django.db import models

from escolas.models import YearField
from pessoas.models.aluno_model import Aluno


class Transporte(models.Model):
    placa = models.CharField(
        max_length=7,
    )
    ano = YearField()
    tipo = models.CharField(
        max_length=20,
        blank=True,
        null=True,
        verbose_name='tipo do veículo',
    )
    nomeMotorista = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        verbose_name='nome do motorista',
    )
    nomeAuxiliar = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        verbose_name='nome do auxiliar',
    )
    itinerario = models.TextField(
        blank=True,
        null=True,
    )
    criado_em = models.DateTimeField(
        auto_now_add=True,
    )
    atualizado_em = models.DateTimeField(
        auto_now=True,
    )
    aluno = models.ManyToManyField(
        Aluno,
        blank=True,
        related_name='alunos_transportes',
    )

    def __str__(self):
        return str(self.placa)

    class Meta:
        unique_together = ['placa', 'ano']