from django.db import models


class Disciplina(models.Model):
    nome = models.CharField(
        max_length=100,
        unique=True,
    )

    def __str__(self):
        return str(self.nome)