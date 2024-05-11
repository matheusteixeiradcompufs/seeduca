from django.db import models

from escolas.models.escola_model import Escola
from escolas.models.item_cardapio_model import ItemCardapioMerenda


class CardapioMerenda(models.Model):
    """
    Representa o cardápio da merenda de uma escola para um determinado dia e turno.

    Cada cardápio é associado a uma escola, contém uma data, um turno (manhã, tarde, noite)
    e uma lista de itens que compõem a merenda.
    """

    TURNO_CHOICES = [
        ('M', 'Manhã'),
        ('T', 'Tarde'),
        ('N', 'Noite'),
    ]
    """
    Escolhas de turno para o cardápio da merenda.
    """

    data = models.DateField()
    """
    A data para a qual o cardápio é válido.
    """

    turno = models.CharField(
        max_length=50,
        choices=TURNO_CHOICES,
    )
    """
    O turno ao qual o cardápio se refere (manhã, tarde, noite).
    """

    itens = models.ManyToManyField(
        ItemCardapioMerenda,
        blank=True,
        related_name='cardapios_itens',
    )
    """
    Os itens que compõem o cardápio da merenda.
    """

    escola = models.ForeignKey(
        Escola,
        on_delete=models.CASCADE,
        related_name='escola_cardapios',
    )
    """
    A escola associada ao cardápio da merenda.
    """

    def __str__(self):
        """
        Retorna uma representação legível do cardápio da merenda.

        Returns:
            str: Uma string contendo a data e o turno do cardápio.
        """
        return 'Cardápio de ' + str(self.data) + ' do turno ' + str(self.turno)

    class Meta:
        """
        Metadados para a classe CardapioMerenda.
        """
        verbose_name = 'cardápio da merenda'
        verbose_name_plural = 'cardápios da merenda'
        unique_together = ['data', 'turno', 'escola']
        """
        Restrição para garantir que cada cardápio seja único para uma data e turno específicos.
        """
