from django.db import models
from escolas.models import Turma
from pessoas.models.pessoa_model import Pessoa


class Funcionario(Pessoa):
    """
    Model para representar um funcionário.

    Atributos:
        formacao (TextField): A formação acadêmica do funcionário.
        retrato (ImageField): A foto do funcionário.
        turmas (ManyToManyField): As turmas associadas ao funcionário.
    """

    formacao = models.TextField(
        null=True,
        blank=True,
        verbose_name='formação acadêmica'
    )
    retrato = models.ImageField(
        upload_to='funcionarios_retratos/',
        blank=True,
        null=True,
        default='',
        verbose_name='retrato'
    )
    turmas = models.ManyToManyField(
        Turma,
        blank=True,
        related_name='turmas_funcionarios',
        verbose_name='turmas'
    )

    def __str__(self):
        """
        Retorna uma representação legível do funcionário.

        Returns:
            str: Uma string representando o funcionário.
        """
        return str(self.usuario)

    class Meta:
        verbose_name = 'funcionário'
        verbose_name_plural = 'funcionários'
