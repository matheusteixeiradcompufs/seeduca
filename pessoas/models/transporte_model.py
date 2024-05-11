from django.db import models

from escolas.models import YearField
from pessoas.models.aluno_model import Aluno


class Transporte(models.Model):
    """
    Modelo que representa um meio de transporte.

    Atributos:
        placa (str): A placa do veículo.
        ano (YearField): O ano do veículo.
        tipo (str): O tipo de veículo.
        nomeMotorista (str): O nome do motorista do veículo.
        nomeAuxiliar (str): O nome do auxiliar do veículo.
        itinerario (str): O itinerário do veículo.
        criado_em (DateTimeField): Data e hora de criação do registro.
        atualizado_em (DateTimeField): Data e hora da última atualização do registro.
        alunos (ManyToManyField): Os alunos associados ao meio de transporte.
    """

    TIPO_TRANSPORTE_CHOICES = [
        ('C', 'CARRO'),
        ('O', 'ÔNIBUS'),
        ('V', 'VAN'),
        ('X', 'OUTROS'),
    ]

    placa = models.CharField(
        max_length=7,
        verbose_name='placa do veículo'  # Nome legível para o campo
    )
    ano = YearField(
        verbose_name='ano do veículo'  # Nome legível para o campo
    )
    tipo = models.CharField(
        max_length=20,
        choices=TIPO_TRANSPORTE_CHOICES,
        verbose_name='tipo do veículo',
    )
    nomeMotorista = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        verbose_name='nome do motorista',
    )
    nomeAuxiliar = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        verbose_name='nome do auxiliar',
    )
    itinerario = models.TextField(
        blank=True,
        null=True,
    )
    criado_em = models.DateTimeField(
        auto_now_add=True,
    )
    atualizado_em = models.DateTimeField(
        auto_now=True,
    )
    alunos = models.ManyToManyField(
        Aluno,
        blank=True,
        related_name='alunos_transportes',
    )

    def __str__(self):
        """
        Retorna uma representação legível do meio de transporte.

        Returns:
            str: Uma string representando a placa do veículo.
        """
        return str(self.placa)

    class Meta:
        # Garante que a placa e o ano sejam únicos juntos
        unique_together = ['placa', 'ano']
