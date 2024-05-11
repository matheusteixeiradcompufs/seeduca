from django.db import models

from escolas.models.base_model import YearField
from escolas.models.disciplina_model import Disciplina
from escolas.models.sala_model import Sala


class Turma(models.Model):
    """
    Representa uma turma em uma escola.

    Cada turma possui um nome, um ano, um turno (manhã, tarde, noite), data e hora de criação,
    data e hora da última atualização, uma sala associada e uma lista de disciplinas.
    """

    TURNO_CHOICES = [
        ('M', 'Manhã'),
        ('T', 'Tarde'),
        ('N', 'Noite'),
    ]
    """
    Escolhas de turno para a turma.
    """

    nome = models.CharField(
        max_length=100,
    )
    """
    O nome da turma.
    """

    ano = YearField()
    """
    O ano ao qual a turma pertence.
    """

    turno = models.CharField(
        max_length=10,
        choices=TURNO_CHOICES,
    )
    """
    O turno da turma (manhã, tarde, noite).
    """

    criada_em = models.DateTimeField(
        auto_now_add=True,
    )
    """
    A data e hora de criação da turma, preenchida automaticamente no momento da criação.
    """

    atualizada_em = models.DateTimeField(
        auto_now=True,
    )
    """
    A data e hora da última atualização da turma, atualizada automaticamente sempre que a turma é modificada.
    """

    sala = models.ForeignKey(
        Sala,
        on_delete=models.PROTECT,
        related_name='sala_turmas',
    )
    """
    A sala associada à turma.
    """

    disciplinas = models.ManyToManyField(
        Disciplina,
        blank=True,
        related_name='disciplinas_turmas',
    )
    """
    As disciplinas oferecidas pela turma.
    """

    def __str__(self):
        """
        Retorna uma representação legível da turma.

        Returns:
            str: Uma string contendo o nome da turma e o ano.
        """
        return f'{str(self.nome)} em {self.ano}'

    class Meta:
        """
        Metadados para a classe Turma.
        """
        unique_together = ['nome', 'ano', 'turno', 'sala', ]
        """
        Restrição para garantir que cada turma seja única para um nome, ano, turno e sala específicos.
        """
