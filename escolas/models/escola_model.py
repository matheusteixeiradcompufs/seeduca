from django.db import models


class Escola(models.Model):
    cnpj = models.CharField(
        max_length=14,
        unique=True,
    )
    nome = models.CharField(
        max_length=100,
    )
    endereco = models.CharField(
        max_length=255,
    )
    num_salas = models.IntegerField(
        default=0,
    )
    quantidade_alunos = models.IntegerField(
        default=0,
    )
    descricao = models.TextField(
        blank=True,
        null=True,
    )
    criado_em = models.DateTimeField(
        auto_now_add=True,
    )
    atualizado_em = models.DateTimeField(
        auto_now=True,
    )
    imagem = models.ImageField(
        upload_to='escolas_images/',
        blank=True,
        null=True,
        default='',
    )

    def __str__(self):
        return str(self.nome)