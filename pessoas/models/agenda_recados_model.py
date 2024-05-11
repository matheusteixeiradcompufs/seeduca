from django.db import models
from pessoas.models.boletim_model import Boletim


class AgendaRecados(models.Model):
    """
    Model para representar a agenda de recados associada a um boletim.

    Atributos:
        boletim (OneToOneField): O boletim associado à agenda de recados.
    """

    boletim = models.OneToOneField(
        Boletim,
        on_delete=models.CASCADE,
        related_name='boletim_agendas',
        verbose_name='boletim',
        help_text='O boletim associado à agenda de recados.'
    )

    def __str__(self):
        """
        Retorna uma representação legível de uma agenda de recados.

        Retorna:
            str: A representação da agenda de recados.
        """
        return f'Agenda de Recados de {self.boletim.turma.ano}'

    class Meta:
        verbose_name = 'agenda de recados'
        verbose_name_plural = 'agendas de recados'
