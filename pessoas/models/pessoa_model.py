from django.contrib.auth.models import User
from django.db import models


class Pessoa(models.Model):
    matricula = models.CharField(
        max_length=10,
        unique=True,
    )
    cpf = models.CharField(
        max_length=11,
        unique=True,
    )
    data_nascimento = models.DateField(
        null=True,
        blank=True,
    )
    endereco = models.CharField(
        max_length=255,
        null=True,
        blank=True,
    )
    uid = models.CharField(
        max_length=100,
        blank=True,
        null=True,
    )
    token = models.CharField(
        max_length=100,
        blank=True,
        null=True,
    )
    criado_em = models.DateTimeField(
        auto_now_add=True,
    )
    atualizado_em = models.DateTimeField(
        auto_now=True,
    )
    usuario = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='usuario_pessoa',
    )

    def __str__(self):
        return str(self.usuario)