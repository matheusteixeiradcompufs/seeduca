from django.db import models

from escolas.models.agenda_escolar_model import AgendaEscolar
from escolas.models.disciplina_model import Disciplina


class DiaAgenda(models.Model):
    """
    Representa um dia específico na agenda escolar de uma turma.

    Cada dia de agenda possui uma data, indicador de utilidade (útil ou não), disciplinas associadas,
    e está vinculado a uma agenda escolar.
    """

    data = models.DateField()
    """
    A data para a qual este dia de agenda é válido.
    """

    util = models.BooleanField(
        default=False,
    )
    """
    Indica se o dia é útil (True) ou não (False).
    """

    disciplinas = models.ManyToManyField(
        Disciplina,
        blank=True,
        related_name='disciplinas_dias',
    )
    """
    As disciplinas associadas a este dia de agenda.
    """

    agenda = models.ForeignKey(
        AgendaEscolar,
        on_delete=models.CASCADE,
        related_name='agenda_dias',
    )
    """
    A agenda escolar à qual este dia de agenda está vinculado.
    """

    criado_em = models.DateTimeField(
        auto_now_add=True,
    )
    """
    A data e hora de criação deste dia de agenda, preenchida automaticamente no momento da criação.
    """

    atualizado_em = models.DateTimeField(
        auto_now=True,
    )
    """
    A data e hora da última atualização deste dia de agenda, atualizada automaticamente sempre que o dia é modificado.
    """

    def __str__(self):
        """
        Retorna uma representação legível da data deste dia de agenda.

        Returns:
            str: Uma string contendo a data deste dia de agenda.
        """
        return str(self.data)

    class Meta:
        """
        Metadados para a classe DiaAgenda.
        """
        verbose_name = 'dia da agenda'
        verbose_name_plural = 'dias da agenda'
        unique_together = ['data', 'agenda']
        """
        Restrição para garantir que cada dia de agenda seja único para uma data e agenda específicas.
        """
