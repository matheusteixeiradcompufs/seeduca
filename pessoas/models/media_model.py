from django.db import models
from escolas.models import Disciplina
from pessoas.models.boletim_model import Boletim


class Media(models.Model):
    """
    Model para representar a média de um aluno em uma disciplina.

    Atributos:
        TIPO_MEDIA_CHOICES (list): Escolhas para o tipo de média.
        tipo (CharField): O tipo de média.
        valor (FloatField): O valor da média.
        criada_em (DateTimeField): Data e hora de criação da média.
        atualizada_em (DateTimeField): Data e hora de atualização da média.
        disciplina (ForeignKey): A disciplina associada à média.
        boletim (ForeignKey): O boletim associado à média.
    """

    TIPO_MEDIA_CHOICES = [
        ('M1', 'Média 1'),
        ('M2', 'Média 2'),
        ('MG', 'Média Geral'),
    ]

    tipo = models.CharField(
        max_length=100,
        choices=TIPO_MEDIA_CHOICES,
        verbose_name='tipo de média'
    )
    valor = models.FloatField(
        default=0,
        verbose_name='valor da média'
    )
    criada_em = models.DateTimeField(
        auto_now_add=True,
        verbose_name='criada em'
    )
    atualizada_em = models.DateTimeField(
        auto_now=True,
        verbose_name='atualizada em'
    )
    disciplina = models.ForeignKey(
        Disciplina,
        on_delete=models.CASCADE,
        related_name='disciplina_medias',
        verbose_name='disciplina'
    )
    boletim = models.ForeignKey(
        Boletim,
        on_delete=models.CASCADE,
        related_name='boletim_medias',
        verbose_name='boletim'
    )

    def __str__(self):
        """
        Retorna uma representação legível da média.

        Returns:
            str: Uma string representando a média.
        """
        return f'{self.tipo} - {self.disciplina} - {self.boletim.aluno}'

    class Meta:
        verbose_name = 'média'
        verbose_name_plural = 'médias'
        unique_together = ['tipo', 'disciplina', 'boletim']
