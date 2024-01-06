from django.db import models

from pessoas.models.aluno_model import Aluno


class Responsavel(models.Model):
    cpf = models.CharField(
        max_length=11,
        unique=True
    )
    nome = models.CharField(
        max_length=255
    )
    observacao = models.TextField()
    aluno = models.ForeignKey(
        Aluno,
        on_delete=models.CASCADE,
        related_name='aluno_responsaveis',
    )

    def __str__(self):
        return str(self.nome)

    class Meta:
        verbose_name = 'responsável'
        verbose_name_plural = 'responsáveis'