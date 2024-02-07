from django.db import models

from escolas.models.escola_model import Escola


class Sala(models.Model):
    numero = models.IntegerField(
        unique=True,
    )
    quantidade_alunos = models.IntegerField(
        null=True,
        blank=True,
    )
    escola = models.ForeignKey(
        Escola,
        on_delete=models.CASCADE,
        related_name='escola_salas',
    )
    criado_em = models.DateTimeField(
        auto_now_add=True,
    )
    atualizado_em = models.DateTimeField(
        auto_now=True,
    )

    def __str__(self):
        return '{:03}'.format(self.numero)

    def save(self, *args, **kwargs):

        quantidade = self.quantidade_alunos

        sala = super().save(*args, **kwargs)

        self.escola.quantidade_alunos = self.escola.quantidade_alunos - quantidade + self.quantidade_alunos

        self.escola.num_salas = len(self.escola.escola_salas)

        return sala

