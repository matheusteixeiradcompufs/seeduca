from django.db import models

from escolas.models import Disciplina
from pessoas.models.boletim_model import Boletim


class Media(models.Model):
    TIPO_MEDIA_CHOICES = [
        ('M1', 'Média 1'),
        ('M2', 'Média 2'),
        ('MG', 'Média Geral'),
    ]

    tipo = models.CharField(
        max_length=100,
        choices=TIPO_MEDIA_CHOICES,
    )
    valor = models.FloatField(
        default=0,
    )
    criada_em = models.DateTimeField(
        auto_now_add=True,
    )
    atualizada_em = models.DateTimeField(
        auto_now=True,
    )
    disciplina = models.ForeignKey(
        Disciplina,
        on_delete=models.CASCADE,
        related_name='disciplina_medias',
    )
    boletim = models.ForeignKey(
        Boletim,
        on_delete=models.CASCADE,
        related_name='boletim_medias',
    )

    def __str__(self):
        return f'{self.tipo} - {self.disciplina} - {self.boletim.aluno}'

    class Meta:
        verbose_name = 'média'
        verbose_name_plural = 'médias'
        unique_together = ['tipo', 'disciplina', 'boletim']