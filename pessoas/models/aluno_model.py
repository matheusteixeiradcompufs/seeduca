from django.db import models
from pessoas.models.pessoa_model import Pessoa


class Aluno(Pessoa):
    """
    Model para representar um aluno.

    Esta model estende a model Pessoa e adiciona campos específicos para alunos.

    Atributos:
        eh_pcd (BooleanField): Um campo booleano que indica se o aluno é uma pessoa com deficiência.
        descricao_pcd (TextField): Um campo de texto para descrever a deficiência do aluno, caso seja uma pessoa com deficiência.
        retrato (ImageField): Um campo de imagem para armazenar o retrato do aluno.
    """

    eh_pcd = models.BooleanField(
        default=False,
        verbose_name='é pessoa com deficiência?',
        help_text='Indica se o aluno é uma pessoa com deficiência.'
    )
    descricao_pcd = models.TextField(
        verbose_name='descrição da deficiência',
        blank=True,
        null=True,
        help_text='Uma descrição da deficiência do aluno, caso seja uma pessoa com deficiência.'
    )
    retrato = models.ImageField(
        upload_to='alunos_retratos/',
        blank=True,
        null=True,
        default='',
        verbose_name='retrato',
        help_text='O retrato do aluno.'
    )

    def __str__(self):
        """
        Retorna uma representação legível de um aluno.

        Retorna:
            str: A representação do aluno.
        """
        return str(self.usuario)
