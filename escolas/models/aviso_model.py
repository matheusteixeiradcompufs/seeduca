from django.db import models

from escolas.models.base_model import AvisoBase
from escolas.models.dia_agenda_model import DiaAgenda


class Aviso(AvisoBase):
    diaAgenda = models.ForeignKey(
        DiaAgenda,
        verbose_name='dia da agenda',
        on_delete=models.CASCADE,
        related_name='dia_avisos',
    )

    def __str__(self):
        return str(self.titulo)