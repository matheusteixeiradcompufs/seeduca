from django.db import models

class ItemCardapioMerenda(models.Model):
    """
    Representa um item que pode estar presente no cardápio da merenda escolar.

    Cada item possui um nome, uma descrição, data e hora de criação e data e hora da última atualização.
    """

    nome = models.CharField(
        max_length=100,
    )
    """
    O nome do item do cardápio.
    """

    descricao = models.TextField()
    """
    A descrição do item do cardápio.
    """

    criado_em = models.DateTimeField(
        auto_now_add=True,
    )
    """
    A data e hora de criação do item do cardápio, preenchida automaticamente no momento da criação.
    """

    atualizado_em = models.DateTimeField(
        auto_now=True,
    )
    """
    A data e hora da última atualização do item do cardápio, atualizada automaticamente sempre que o item é modificado.
    """

    def __str__(self):
        """
        Retorna uma representação legível do nome do item do cardápio.

        Returns:
            str: O nome do item do cardápio.
        """
        return str(self.nome)

    class Meta:
        """
        Metadados para a classe ItemCardapioMerenda.
        """
        verbose_name = 'ítem do cardápio'
        """
        Um nome mais descritivo para este modelo na interface de administração.
        """
        verbose_name_plural = 'ítens do cardápio'
        """
        Um nome mais descritivo para a versão plural deste modelo na interface de administração.
        """
