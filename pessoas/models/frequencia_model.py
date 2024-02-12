from django.db import models


class Frequencia(models.Model):
    percentual = models.FloatField(
        default=0,
    )

    def __str__(self):
        return f'Frequência de {self.frequencia_boletim.aluno} em {self.frequencia_boletim.ano}'

    class Meta:
        verbose_name = 'frequência'