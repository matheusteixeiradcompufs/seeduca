from django.db import models
from pessoas.models import Boletim


class Frequencia(models.Model):
    """
    Model para representar a frequência de um aluno em um boletim.

    Atributos:
        percentual (float): O percentual de presença do aluno.
        boletim (OneToOneField): A referência ao boletim associado à frequência.
    """

    percentual = models.FloatField(
        default=0,
        verbose_name='percentual'
    )
    boletim = models.OneToOneField(
        Boletim,
        on_delete=models.CASCADE,
        related_name='boletim_frequencia',
        verbose_name='boletim'
    )

    def __str__(self):
        """
        Retorna uma representação legível da frequência do aluno.

        Returns:
            str: Uma string representando a frequência do aluno.
        """
        return f'Frequência de {self.boletim.aluno} em {self.boletim.turma.ano} da turma {self.boletim.turma}'

    class Meta:
        verbose_name = 'frequência'
