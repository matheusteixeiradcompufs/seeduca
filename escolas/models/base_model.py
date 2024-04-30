from django.db import models


class YearField(models.IntegerField):
    def __init__(self, *args, **kwargs):
        kwargs['validators'] = []
        kwargs['choices'] = [(i, i) for i in range(1900, 2101)]
        super().__init__(*args, **kwargs)


class Telefone(models.Model):
    numero = models.CharField(
        max_length=20,
    )

    def __str__(self):
        return str(self.numero)


class Email(models.Model):
    endereco = models.EmailField()

    def __str__(self):
        return str(self.endereco)


class AvisoBase(models.Model):
    titulo = models.CharField(
        max_length=100,
    )
    texto = models.TextField()
    publicado_em = models.DateTimeField(
        auto_now_add=True,
    )
    atualizado_em = models.DateTimeField(
        auto_now=True,
    )
