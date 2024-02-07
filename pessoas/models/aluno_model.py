from django.db import models

from escolas.models import Turma
from pessoas.models.pessoa_model import Pessoa


class Aluno(Pessoa):
    eh_pcd = models.BooleanField(
        default=False,
    )
    descricao_pcd = models.TextField(
        verbose_name='descrição da pcd',
        blank=True,
        null=True,
    )
    retrato = models.ImageField(
        upload_to='alunos_retratos/',
        blank=True,
        null=True,
        default='',
    )
    turmas = models.ManyToManyField(
        Turma,
        blank=True,
        related_name='turmas_alunos',
    )

    def __str__(self):
        return str(self.usuario)