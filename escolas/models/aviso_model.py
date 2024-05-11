from django.db import models

from escolas.models.base_model import AvisoBase
from escolas.models.dia_agenda_model import DiaAgenda


class Aviso(AvisoBase):
    """
    Representa um aviso associado a um dia específico da agenda.

    Herda de AvisoBase.
    """

    diaAgenda = models.ForeignKey(
        DiaAgenda,
        verbose_name='dia da agenda',
        on_delete=models.PROTECT,
        related_name='dia_avisos',
    )
    """
    O dia da agenda ao qual este aviso está vinculado.
    """

    def __str__(self):
        """
        Retorna uma representação legível do título do aviso.
        """
        return str(self.titulo)