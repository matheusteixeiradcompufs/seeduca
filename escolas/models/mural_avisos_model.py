from django.db import models

from escolas.models.base_model import YearField
from escolas.models.escola_model import Escola


class MuralAvisos(models.Model):
    """
    Representa o mural de avisos de uma escola para um determinado ano.

    Cada mural de avisos está associado a uma escola específica e a um ano específico.
    """

    ano = YearField()
    """
    O ano ao qual o mural de avisos se refere.
    """

    escola = models.ForeignKey(
        Escola,
        on_delete=models.CASCADE,
        related_name='escola_murais',
    )
    """
    A escola associada ao mural de avisos.
    """

    def __str__(self):
        """
        Retorna uma representação legível do mural de avisos.

        Returns:
            str: Uma string contendo o nome da escola e o ano do mural de avisos.
        """
        return f'Mural de avisos da {self.escola} em {self.ano}'

    class Meta:
        """
        Metadados para a classe MuralAvisos.
        """
        verbose_name = 'mural de avisos'
        """
        Um nome mais descritivo para este modelo na interface de administração.
        """
        verbose_name_plural = 'Murais de avisos'
        """
        Um nome mais descritivo para a versão plural deste modelo na interface de administração.
        """
        unique_together = ['ano', 'escola', ]
        """
        Restrição para garantir que cada mural de avisos seja único para um ano e uma escola específicos.
        """
