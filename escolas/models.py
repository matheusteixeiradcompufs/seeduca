from django.db import models
from django.utils import timezone


class Escola(models.Model):
    cnpj = models.CharField(max_length=14, unique=True)
    nome = models.CharField(max_length=100)
    endereco = models.CharField(max_length=255)
    num_salas = models.IntegerField(blank=True, null=True)
    descricao = models.TextField(blank=True, null=True)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)
    imagem = models.ImageField(upload_to=f'escola_images/', blank=True, null=True, default='')

    def __str__(self):
        return self.nome

    def save(self, *args, **kwargs):
        self.atualizado_em = timezone.now()
        if not self.pk:
            self.criado_em = timezone.now()
        super().save(*args, **kwargs)


class Telefone(models.Model):
    numero = models.CharField(max_length=20)
    escola = models.ForeignKey(Escola, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.numero


class Email(models.Model):
    endereco = models.EmailField()
    escola = models.ForeignKey(Escola, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.endereco