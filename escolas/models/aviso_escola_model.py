from django.db import models

from escolas.models.base_model import AvisoBase
from escolas.models.mural_avisos_model import MuralAvisos


class AvisoEscola(AvisoBase):
    mural = models.ForeignKey(MuralAvisos, verbose_name='mural de avisos', on_delete=models.CASCADE, related_name='mural_avisos')

    def __str__(self):
        return str(self.titulo)