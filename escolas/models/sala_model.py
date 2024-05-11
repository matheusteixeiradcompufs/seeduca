from django.db import models

from escolas.models.escola_model import Escola


class Sala(models.Model):
    """
    Representa uma sala em uma escola.

    Cada sala é identificada por um número único e possui uma quantidade de alunos associada.
    """

    numero = models.IntegerField()
    """
    O número da sala.
    """

    quantidade_alunos = models.IntegerField(
        default=0,
    )
    """
    A quantidade de alunos na sala.
    """

    escola = models.ForeignKey(
        Escola,
        on_delete=models.PROTECT,
        related_name='escola_salas',
    )
    """
    A escola à qual a sala pertence.
    """

    criado_em = models.DateTimeField(
        auto_now_add=True,
    )
    """
    A data e hora de criação da sala, preenchida automaticamente no momento da criação.
    """

    atualizado_em = models.DateTimeField(
        auto_now=True,
    )
    """
    A data e hora da última atualização da sala, atualizada automaticamente sempre que a sala é modificada.
    """

    def __str__(self):
        """
        Retorna uma representação legível do número da sala.

        Returns:
            str: O número da sala.
        """
        return '{:03}'.format(self.numero)

    class Meta:
        """
        Metadados para a classe Sala.
        """
        unique_together = ['numero', 'escola']
        """
        Restrição para garantir que cada número de sala seja único para uma escola específica.
        """

    def save(self, *args, **kwargs):
        """
        Salva a sala e atualiza a quantidade de alunos na escola.

        Este método também atualiza o número total de salas na escola.

        Args:
            *args: Argumentos posicionais adicionais.
            **kwargs: Argumentos de palavra-chave adicionais.
        """
        quantidade_anterior = 0

        if self.pk:
            # Se a instância já existe, obter a quantidade anterior de alunos
            sala_anterior = Sala.objects.get(pk=self.pk)
            quantidade_anterior = sala_anterior.quantidade_alunos

        # Salvar a instância
        super(Sala, self).save(*args, **kwargs)

        # Atualizar a quantidade de alunos na escola
        diferenca_quantidade = self.quantidade_alunos - quantidade_anterior
        self.escola.quantidade_alunos += diferenca_quantidade
        self.escola.save()

        # Atualizar o número de salas na escola
        self.escola.num_salas = self.escola.escola_salas.count()
        self.escola.save()

        return
