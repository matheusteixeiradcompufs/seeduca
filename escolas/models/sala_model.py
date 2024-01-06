from django.db import models

from escolas.models.escola_model import Escola


class Sala(models.Model):
    numero = models.IntegerField(unique=True)
    quantidade_alunos = models.IntegerField(null=True, blank=True)
    escola = models.ForeignKey(Escola, on_delete=models.CASCADE, related_name='escola_salas')

    def __str__(self):
        return '{:03}'.format(self.numero)