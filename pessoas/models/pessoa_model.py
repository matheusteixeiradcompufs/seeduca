from django.contrib.auth.models import User
from django.db import models


class Pessoa(models.Model):
    """
    Modelo que representa uma pessoa.

    Atributos:
        matricula (CharField): A matrícula da pessoa.
        cpf (CharField): O CPF da pessoa.
        data_nascimento (DateField): A data de nascimento da pessoa.
        endereco (CharField): O endereço da pessoa.
        uid (CharField): O identificador único da pessoa.
        token (CharField): O token da pessoa.
        criado_em (DateTimeField): Data e hora de criação da pessoa.
        atualizado_em (DateTimeField): Data e hora de atualização da pessoa.
        usuario (OneToOneField): O usuário associado à pessoa.
    """

    matricula = models.CharField(
        max_length=10,
        unique=True,
        verbose_name='matrícula'
    )
    cpf = models.CharField(
        max_length=11,
        unique=True,
        verbose_name='CPF'
    )
    data_nascimento = models.DateField(
        null=True,
        blank=True,
        verbose_name='data de nascimento'
    )
    endereco = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        verbose_name='endereço'
    )
    uid = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        verbose_name='UID'
    )
    token = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        verbose_name='token'
    )
    criado_em = models.DateTimeField(
        auto_now_add=True,
        verbose_name='criado em'
    )
    atualizado_em = models.DateTimeField(
        auto_now=True,
        verbose_name='atualizado em'
    )
    usuario = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='usuario_pessoa',
        verbose_name='usuário'
    )

    def __str__(self):
        """
        Retorna uma representação legível da pessoa.

        Returns:
            str: Uma string representando a pessoa.
        """
        return str(self.usuario)
