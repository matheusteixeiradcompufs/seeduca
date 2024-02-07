from django.db import models

from escolas.models.escola_model import Escola
from escolas.models.item_cardapio_model import ItemCardapioMerenda


class CardapioMerenda(models.Model):
    TURNO_CHOICES = [
        ('M', 'Manhã'),
        ('T', 'Tarde'),
        ('N', 'Noite'),
    ]

    data = models.DateField()
    turno = models.CharField(
        max_length=50,
        choices=TURNO_CHOICES,
    )
    itens = models.ManyToManyField(
        ItemCardapioMerenda,
        blank=True,
        related_name='cardapios_itens',
    )
    escola = models.ForeignKey(
        Escola,
        on_delete=models.CASCADE,
        related_name='escola_cardapios',
    )

    def __str__(self):
        return 'Cardápio de ' + str(self.data) + ' do turno ' + str(self.turno)

    class Meta:
        verbose_name = 'cardápio da merenda'
        verbose_name_plural = 'cardápios da merenda'
        unique_together = ['data', 'turno']