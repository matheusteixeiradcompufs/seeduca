from django.db import models

from pessoas.models.aluno_model import Aluno


class Responsavel(models.Model):
    """
    Modelo que representa um responsável por um aluno.

    Atributos:
        cpf (CharField): O CPF do responsável.
        nome (CharField): O nome do responsável.
        observacao (TextField): Observações sobre o responsável.
        aluno (ForeignKey): O aluno associado ao responsável.
    """

    cpf = models.CharField(
        max_length=11,
        unique=True,
        verbose_name='CPF'
    )
    nome = models.CharField(
        max_length=255,
        verbose_name='nome'
    )
    observacao = models.TextField(
        verbose_name='observação'
    )
    aluno = models.ForeignKey(
        Aluno,
        on_delete=models.CASCADE,
        related_name='aluno_responsaveis',
        verbose_name='aluno'
    )

    def __str__(self):
        """
        Retorna uma representação legível do responsável.

        Returns:
            str: Uma string representando o responsável.
        """
        return str(self.nome)

    class Meta:
        verbose_name = 'responsável'
        verbose_name_plural = 'responsáveis'
