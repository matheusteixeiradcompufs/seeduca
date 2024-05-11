from django.db import models

from escolas.models.base_model import AvisoBase
from escolas.models.mural_avisos_model import MuralAvisos


class AvisoEscola(AvisoBase):
    """
    Representa um aviso específico para uma escola.

    Herda de AvisoBase.
    """

    mural = models.ForeignKey(
        MuralAvisos,
        verbose_name='mural de avisos',
        on_delete=models.PROTECT,
        related_name='mural_avisos',
    )
    """
    O mural de avisos ao qual este aviso está vinculado.
    """

    def __str__(self):
        """
        Retorna uma representação legível do título do aviso.
        """
        return str(self.titulo)

    class Meta:
        """
        Metadados para a classe AvisoEscola.
        """
        verbose_name = 'aviso da escola'
        verbose_name_plural = 'Avisos da escola'
