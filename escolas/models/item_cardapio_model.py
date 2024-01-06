from django.db import models


class ItemCardapioMerenda(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()

    def __str__(self):
        return str(self.nome)

    class Meta:
        verbose_name = 'ítem do cardápio'
        verbose_name_plural = 'ítens do cardápio'