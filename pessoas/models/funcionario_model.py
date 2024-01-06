from django.db import models

from escolas.models import Turma
from pessoas.models.pessoa_model import Pessoa


class Funcionario(Pessoa):
    formacao = models.TextField(
        null=True,
        blank=True
    )
    turma = models.ManyToManyField(
        Turma,
        blank=True,
        related_name='turmas_funcionarios'
    )

    def __str__(self):
        return str(self.usuario)

    class Meta:
        verbose_name = 'funcionário'